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

"""A template task with a ball that should touch left or right wall."""

## color vs. position.

import numpy as np
import phyre.creator as creator_lib

import random


@creator_lib.define_task_template(

    # ratio of width
    ball_x=np.linspace(0.1, 0.9, 32),

    # distance from the shelf
    ball_y=np.linspace(0.3, 0.8, 8),
    ball_r=np.linspace(0.05, 0.12, 5),
    search_params=dict(
        max_search_tasks=800,
        required_flags=['BALL:GOOD_STABLE'],
        diversify_tier='ball'
    ),
    left=[True, False],
    over=[True, False],
    version='6',
)
def build_task(C, ball_x, ball_y, ball_r, left, over):

    # target wall size


    if left:
        target_floor= C.add('static bar', scale=0.5, left=0, bottom=0)
        C.add('static bar', scale=0.5, right=C.scene.width, bottom=0)
    else:
        target_floor= C.add('static bar', scale=5.0, right=C.scene.width, bottom=0)
        C.add('static bar', scale=0.5, left=0, bottom=0)

    # ball can get in the ramp
    #shelf_size = 0.50 - ball_r * 2

    # horizontal shelf
    #shelf = C.add('static bar', shelf_size, center_x=C.scene.width / 2, top=20)

    # ramp shelf
    left_ramp = C.add('static bar', 0.35, angle=10, right=C.scene.width / 2, bottom=target_floor.top)
    right_ramp = C.add('static bar',  0.35, angle=-10, left=C.scene.width / 2, bottom=target_floor.top)

    eps=0.01
    if not over:
        if left:

            shape_x = random.uniform(0+eps,(left_ramp.right/C.scene.width)-eps)
            shape = C.add(
                'dynamic ball',
                ball_r,
                left=shape_x * C.scene.width,
                bottom=ball_y * C.scene.height)

        else:

            shape_x = random.uniform((right_ramp.left/C.scene.width)+eps,1-eps)
            shape = C.add(
                'dynamic ball',
                ball_r,
                left=shape_x * C.scene.width,
                bottom=ball_y * C.scene.height)
    else:

        if left:
            shape_x = random.uniform((right_ramp.left/C.scene.width)+eps,1-eps)
            shape = C.add(
                'dynamic ball',
                ball_r,
                left=shape_x * C.scene.width,
                bottom=ball_y * C.scene.height)
        else:

            shape_x = random.uniform(0,(left_ramp.right/C.scene.width)-eps)
            shape = C.add(
                'dynamic ball',
                ball_r,
                left=shape_x * C.scene.width,
                bottom=ball_y * C.scene.height)


    # if shape.right>=C.scene.width or shape.left<=0:
    #     raise creator_lib.SkipTemplateParams


    # if ball.center_x <= shelf.left or ball.center_x >= shelf.right:
    #     raise creator_lib.SkipTemplateParams
    # if abs(ball.center_x - target_wall.center_x) > C.scene.width * .7:
    #     raise creator_lib.SkipTemplateParams

    # what is success in this scenario
    C.update_task(
        body1=shape,
        body2=target_floor,
        relationships=[C.SpatialRelationship.TOUCHING],
        over = over)

    C.set_meta(C.SolutionTier.BALL)
