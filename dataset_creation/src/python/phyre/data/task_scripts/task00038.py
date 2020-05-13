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

"""Funnel a ball onto a target floor pad."""
import numpy as np
import phyre.creator as creator_lib
import random


@creator_lib.define_task_template(
    ball_x=np.linspace(0.4, 0.6, 20),
    angle=np.linspace(20, 30, 10),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball',
    ),
    over=[True, False],
    max_tasks=100,
    version='3',
)
def build_task(C, ball_x, angle, over):
    # Put ball on bar.




    target = C.add('static bar', 1, bottom=0, left=0)

    # floor = C.add('static bar', scale=0.8) \
    #          .set_bottom(0)
    # box = C.add('static bar', scale=0.2) \
    #        .set_bottom(target.top)


    bar_scale = 0.5
    left_bar = C.add('static bar', scale=bar_scale, angle=-angle) \
                .set_left(0) \
                .set_top(C.scene.height * 0.9)

    right_bar = C.add('static bar', scale=bar_scale, angle=angle) \
                .set_right(C.scene.width) \
                .set_top(C.scene.height * 0.9)

    gap = (right_bar.left - left_bar.right)/C.scene.width
    ball_top = random.uniform(0.9,1)
    if over:

        ball_scale = random.uniform(gap,0.15)
        ball = C.add('dynamic ball', scale=ball_scale) \
                .set_top(ball_top*C.scene.height) \
                .set_center_x(ball_x * C.scene.width)
    else:

        ball_scale = random.uniform(0.02,gap)
        ball = C.add('dynamic ball', scale=ball_scale) \
                .set_top(ball_top*C.scene.height) \
                .set_center_x(ball_x * C.scene.width)

    # gap = right_bar.left - left_bar.right
    # if gap <= ball_scale * C.scene.height:
    #     raise creator_lib.SkipTemplateParams

    C.update_task(
        body1=ball,
        body2=target,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)
