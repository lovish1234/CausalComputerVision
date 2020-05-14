# Original task 1
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
    ball_r=np.linspace(0.03, 0.15, 10),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball'
    ),
    over=[True, False],
    max_tasks=20)
def build_task(C, ball_r, over):

    ball_height = random.uniform(ball_r, 1.-ball_r)
    ball_height *= C.scene.height
    if over:
        # ball over the obstacle
        center_ball = random.uniform(ball_r, 0.5 - ball_r)
        center_ball *= C.scene.width
        ball = C.add('dynamic ball', ball_r) \
            .set_center_x(center_ball) \
            .set_center_y(ball_height) \
            .set_color('blue')
    else:
        # ball not over the obstacle
        center_ball = random.uniform(0.5 + ball_r, 1. - ball_r)
        center_ball *= C.scene.width
        #print (over, obstacle_x/C.scene.width , obstacle_x/C.scene.width + obstacle_width, center_ball/C.scene.width)
        ball = C.add('dynamic ball', ball_r) \
            .set_center_x(center_ball) \
            .set_center_y(ball_height) \
            .set_color('green')

    # Add a dynamic ball

    # target object
    bottom_wall = C.add('static bar', 0.5, bottom=0, left=0)

    # Create assignment.
    C.update_task(
        body1=ball,
        body2=bottom_wall,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)
