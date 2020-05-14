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

"""Template task in which the agent should knock a vertical bar against the wall."""
import numpy as np
import phyre.creator as creator_lib
import random


@creator_lib.define_task_template(
    bar_scale=np.linspace(0.2, 0.6, 4),
    wall_scale=np.linspace(0.4,1.0,10),
    position=["Left", "Right"],
    over=[True, False],
    search_params=dict(
        max_search_tasks=800,
        required_flags=['BALL:GOOD_STABLE'],
        diversify_tier='ball'
    ),
    max_tasks=100,
    version='2')
def build_task(C, bar_scale, wall_scale, over, position):



    if over:
        if position=="Left":
            bar = C.add(
                'dynamic bar',
                scale=bar_scale,
                angle=90,
                center_x=C.scene.width*(random.uniform(0.05, bar_scale/2)),
                bottom=0)
        else:
            bar = C.add(
                'dynamic bar',
                scale=bar_scale,
                angle=90,
                center_x=C.scene.width-C.scene.width*(random.uniform(0.05, bar_scale/2)),
                bottom=0)
        wall = C.add('static bar', scale=wall_scale, left=0, angle=90, bottom=0)

    else:
        if position=="Left":
            angle = random.randint(95,110)
            bar = C.add(
                'dynamic bar',
                scale=bar_scale,
                angle=angle,
                center_x=C.scene.width*(random.uniform(0.1, bar_scale/2)),
                bottom=0)
            wall = C.add('static bar', scale=wall_scale, left=0, angle=90, bottom=0)
        else:
            angle = random.randint(70,85)
            bar = C.add(
                'dynamic bar',
                scale=bar_scale,
                angle=angle,
                center_x=C.scene.width-C.scene.width*(random.uniform(0.1, bar_scale/2)),
                bottom=0)
            wall = C.add('static bar', scale=wall_scale, right=C.scene.width, angle=90, bottom=0)




    # Create assignment:

    C.update_task(
        body1=bar, body2=wall, relationships=[C.SpatialRelationship.TOUCHING], over=over)
    C.set_meta(C.SolutionTier.BALL)
