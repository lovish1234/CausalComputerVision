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
    obstacle_width=__OBSTACLE_WIDTHS,
    obstacle_x=__OBSTACLE_XS,
    obstacle_y=__OBSTACLE_YS,
    ball_r=np.linspace(0.03, 0.09, 5),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball'
    ),
    over=[True, False],
    max_tasks=100)

def build_task(C, obstacle_width, obstacle_x, obstacle_y, ball_r, over):
    # Add obstacle.
    if obstacle_x + obstacle_width > 1.:
        raise creator_lib.SkipTemplateParams

    left_limit = obstacle_x 
    right_limit = obstacle_x + obstacle_width

    # multiply with width and height to get absolute values
    obstacle_x *= C.scene.width
    obstacle_y *= C.scene.height
    #red = color_to_id('red')

    obstacle = C.add('static bar', scale=obstacle_width) \
                .set_left(obstacle_x) \
                .set_bottom(obstacle_y) 

    if over:
        # ball over the obstacle
        center_ball = obstacle_x + obstacle.width / 2.

        ball = C.add('dynamic ball', ball_r) \
            .set_center_x(center_ball) \
            .set_bottom(0.9 * C.scene.height) \
            .set_color('blue')
        #print (over, obstacle_x/C.scene.width + obstacle_width/2.0, center_ball/C.scene.width)
    else:
        # ball not over the obstacle
        
        center_ball_list = []
        if ball_r < left_limit-ball_r:
            left_intervel_random = random.uniform(ball_r,left_limit-ball_r)
            center_ball_list.append(left_intervel_random)
        if right_limit+ball_r < 1.0-ball_r:
            right_intervel_random = random.uniform(right_limit+ball_r,1.0-ball_r)
            center_ball_list.append(right_intervel_random)

        center_ball = np.random.choice(center_ball_list)

        # pick a point randomly between 0 and 1
        # such that it does not fall between left
        # and right limit 

        center_ball*=C.scene.width
        #print (over, obstacle_x/C.scene.width , obstacle_x/C.scene.width + obstacle_width, center_ball/C.scene.width)
        ball = C.add('dynamic ball', ball_r) \
            .set_center_x(center_ball) \
            .set_bottom(0.9 * C.scene.height) \
            .set_color('green')

    # Add a dynamic ball

    # target object
    bottom_wall = C.add('static bar', 1, bottom=0, left=0)

    # Create assignment.
    C.update_task(
        body1=ball,
        body2=bottom_wall,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)