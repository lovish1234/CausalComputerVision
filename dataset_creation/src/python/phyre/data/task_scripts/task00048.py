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

"""Template task with a ball that must not roll of a cliff."""
import numpy as np
import phyre.creator as creator_lib
import random

@creator_lib.define_task_template(
    bar_y=np.linspace(0.1, 0.5, 10),
    angle_right=np.linspace(5, 20, 5),
    length_left=np.linspace(0.2, 0.8, 4),
    search_params=dict(
        max_search_tasks=1000,
        required_flags=['BALL:GOOD_STABLE'],
        diversify_tier='ball'

    ),
    over=[True,False],
    version='4')
def build_task(C, bar_y,  angle_right, length_left, over):

    # Add obstacle bars.
    scene_width = C.scene.width
    scene_height = C.scene.height

    left_bar = C.add('static bar', scale=length_left) \
                .set_angle(-angle_right) \
                .set_bottom((bar_y + .2) * scene_height) \
                .set_left(-0.01 * scene_width)

    shape_x = random.uniform(0,left_bar.right/scene_width)

    if over:
        shape = C.add('dynamic box', scale=0.1) \
                .set_center_x(shape_x * scene_width) \
                .set_bottom(0.85 * scene_height)  \
                .set_angle(-angle_right)      
    else:
        # Add ball.
        shape = C.add('dynamic ball', scale=0.1) \
                .set_center_x(shape_x * scene_width) \
                .set_bottom(0.85 * scene_height)

    if shape.left >= left_bar.right or shape.left<=0 or shape.bottom<=left_bar.top:
        raise creator_lib.SkipTemplateParams

    # target wall
    bottom_wall = C.add('static bar', 1.0, left=0, bottom=0)


    # Create assignment.
    C.update_task(
        body1=shape,
        body2=bottom_wall,
        relationships=[C.SpatialRelationship.TOUCHING])
    C.set_meta(C.SolutionTier.BALL)
