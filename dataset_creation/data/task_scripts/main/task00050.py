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
    bar_y=range(10),
    vbar_x_scale=np.linspace(0.5, 0.6, 4),
    angle=np.linspace(35, 55, 10),
    distance_to_wall=np.linspace(0.01, 0.05, 2),
    version='3',
    over=[True, False],
)
def build_task(C, bar_y, vbar_x_scale, distance_to_wall, angle, over):

    vbar_x = vbar_x_scale * C.scene.width
    # Add ball on the left.

    if over:
        eps=random.uniform(5,15)
        bar_dynamic = C.add(
            'dynamic bar',
            scale=0.15,
            angle=eps,
            center_x=0.5*C.scene.height,
            bottom=0.8 * C.scene.height)
    else:
        eps=random.uniform(0,5)
        bar_dynamic = C.add(
            'dynamic bar',
            scale=0.15,
            angle=-angle+eps,
            center_x=0.5*C.scene.height,
            bottom=0.8 * C.scene.height)

    # Add diagonal bars.
    bars = []
    for i in range(10):
        bar = C.add(
            'static bar',
            scale=0.25,
            angle=-angle,
            bottom=0.3*C.scene.height,
            right=(i * 0.15) * C.scene.width)
        if bar.bottom > 0:
            bars.append(bar)
    #.set_left(bars[0].right + 1)




    bottom_wall = C.add('static bar', 1, bottom=0, left=0)

    # Create assignment.
    C.update_task(
        body1=bar_dynamic,
        body2=bottom_wall,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)
