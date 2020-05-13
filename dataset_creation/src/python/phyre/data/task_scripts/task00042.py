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

import phyre.creator as creator_lib
import numpy as np
import random


@creator_lib.define_task_template(
    bar_y=np.linspace(0.4, 0.7, 10),
    bottom_jar_scale=np.linspace(0.15, 0.20, 3),
    bottom_jar_x=np.linspace(0.25, 0.50, 5),
    left_diag_angle=np.linspace(30, 70, 3),
    right_diag_angle=np.linspace(30, 70, 3),
    max_tasks=100,
    search_params=dict(required_flags=['TWO_BALLS:GOOD_STABLE']),
    version='2',
    over=[True, False],
)
def build_task(C, bar_y, bottom_jar_scale, bottom_jar_x, left_diag_angle,
               right_diag_angle, over):


    # Add jar on top of bar.
    ground = C.add('static bar',
                   scale=1.0,
                   bottom=0,
                   left=0)

    if over:

        cover = C.add(
            'dynamic jar',
            scale=random.uniform(0.2, 0.5),
            angle=180.0,
            left=128,
            top=C.scene.height)
        ball = C.add(
            'dynamic ball',
            scale=random.uniform(0.02,0.08),
            center_x=cover.left + cover.width * 0.5,
            bottom=ground.top)
    else:
        scale = random.uniform(0.2, 0.5)
        cover = C.add(
            'dynamic jar',
            scale=scale,
            angle=180.0,
            left=128,
            top=C.scene.height)
        ball = C.add(
            'dynamic ball',
            scale=2.0*scale/3.0,
            center_x=cover.left + cover.width * 0.5,
            bottom=ground.top)


    # create assignment:
    C.update_task(
        body1=ball,
        body2=cover,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)
