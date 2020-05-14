# Original task 2
# May randomize the position of ball over the slab


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

"""Template task with a ball that should avoid an obstacle bar to hit ground."""
import phyre.creator as creator_lib
import random
import numpy as np

__OBSTACLE_WIDTHS = [val * 0.1 for val in range(1, 8)]
__OBSTACLE_YS = [val * 0.1 for val in range(3, 8)]
__OBSTACLE_XS = [val * 0.1 for val in range(0, 11)]


@creator_lib.define_task_template(
    ball_r=np.linspace(0.03, 0.09, 5),
    ball_y = np.linspace(0.6, 0.9, 5),
    ball_x = np.linspace(0.1, 0.35, 5),
    scale_platform = np.linspace(0.15 ,0.30, 5),
    scale_lower_platform = np.linspace(0.25 ,0.40, 5),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball'
    ),
    over=[True, False],
    max_tasks=100)

def build_task(C,  ball_r, ball_x, ball_y, scale_platform, scale_lower_platform, over):
    # Add obstacle.


    # target object
    bottom_wall = C.add('static bar', 1, bottom=0, left=0)

    shape1 = C.add(
            'static rectbox',
            scale=scale_lower_platform,
            angle=90,
            left=0,
            bottom=bottom_wall.top)

    # platform on one side
    shape2 = C.add(
            'static rectbox',
            scale=scale_platform,
            right=C.scene.width,
            bottom=bottom_wall.top)

    # ramp on top of the shape
    ramp = C.add(
            'static isotriangle',
            scale=scale_lower_platform,
            left=0,
            bottom=shape1.top)

    # fulcrum bar
    fulcrum_bar = C.add(
            'dynamic bar',
            scale=scale_platform*2.35,
            angle=0,
            right=C.scene.width,
            bottom=shape2.top)
    # ball
    ball_x = random.uniform(0, ramp.right)

    ball = C.add(
            'dynamic ball',
            scale=ball_r,
            left = ball_x,
            bottom=ball_y*C.scene.height)

    if shape1.top > shape2.top - 50:
         raise creator_lib.SkipTemplateParams

    if over:
        cause_x = random.uniform(fulcrum_bar.left/C.scene.width+0.15, shape2.left/C.scene.width)
        cause_object = C.add(
            'dynamic ball',
            scale=0.15,
            right = cause_x*C.scene.width,
            bottom=fulcrum_bar.top)
    else:
        cause_x = random.uniform(shape2.left/C.scene.width,0.85)
        cause_object = C.add(
            'dynamic ball',
            scale=0.15,
            left = cause_x*C.scene.width,
            bottom=fulcrum_bar.top)




    # Add a dynamic ball



    # Create assignment.
    C.update_task(
        body1=ball,
        body2=bottom_wall,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)