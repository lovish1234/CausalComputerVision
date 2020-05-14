# Copyright (c) Facebook, Inc. and its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Template task in which two balls should touch each other."""
import numpy as np
import phyre.creator as creator_lib
import random


@creator_lib.define_task_template(
    shape_x=np.linspace(0.4, 0.6, 20),
    angle=np.linspace(20, 40, 10),
    #shape_scale=np.linspace(0.06, 0.12, 3),
    search_params=dict(required_flags=['BALL:GOOD_STABLE']),
    version='2',
    over=[True, False],
    max_tasks=100,
)

def build_task(C,shape_x, angle, over):

    # Task definition is symmetric.
    target = C.add('static bar', 1, bottom=0, left=0)


    bar_scale = 0.5
    left_bar = C.add('static bar', scale=bar_scale, angle=-angle) \
                .set_left(0) \
                .set_top(C.scene.height * 0.6)
    right_bar = C.add('static bar', scale=bar_scale, angle=angle) \
                .set_right(C.scene.width) \
                .set_top(C.scene.height * 0.6)

    gap = (right_bar.left - left_bar.right)/C.scene.width
    shape_top = random.uniform(0.6,1)


    if over:
        # add a box, difficult to roll over
        eps=0.01
        shape_scale = random.uniform(0.02,gap-eps)
        shape = C.add(
            'dynamic box',
            scale=3*shape_scale/2.,
            left=shape_x*C.scene.width,
            bottom=shape_top*C.scene.height)


    else:
        shape_scale = random.uniform(gap,0.20)
        # add a ball, can easily roll over
        shape = C.add('dynamic ball', scale=shape_scale) \
                .set_top(shape_top*C.scene.height) \
                .set_center_x(shape_x * C.scene.width)

    if shape.top >= C.scene.height:
        raise creator_lib.SkipTemplateParams
    if shape.left <= 0:
        raise creator_lib.SkipTemplateParams
    if shape.right >= C.scene.width-1:
        raise creator_lib.SkipTemplateParams


    # Create assignment:
    C.update_task(
        body1=shape,
        body2=target,
        relationships=[C.SpatialRelationship.TOUCHING],
        )
    C.set_meta(C.SolutionTier.BALL)
