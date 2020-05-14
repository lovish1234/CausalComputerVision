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
    right_bar_angle=np.linspace(30, 50, 6),
    center_point=np.linspace(0.5, 0.8, 6),
    left_bar_angle=np.linspace(100, 140, 5),
    objectx_vertical_top_offset=np.linspace(15, 35, 3),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball',
        max_search_tasks=540,
    ),
    over = [True, False],
    version='5',
)
def build_task(C, right_bar_angle, objectx_vertical_top_offset, center_point,
               left_bar_angle, over):
    
    floor = C.add(
        'static bar',
        scale = 1.0,
        left = 0,
        bottom = 0)

    bar_right = C.add(
        'static bar',
        scale=1.0,
        angle=right_bar_angle,
        left=C.scene.width * center_point,
        bottom=floor.top)

    bar_left = C.add(
        'static bar',
        scale=1.0,
        angle=left_bar_angle,
        right=bar_right.left-8,
        bottom=floor.top)

    offset = 0
    if bar_right.right < C.scene.width:
        offset = C.scene.width - bar_right.right
    elif bar_left.left > 0:
        offset = -bar_left.left
    for body in [bar_right, bar_left]:
        body.set_left(body.left + offset)

    if over:
        objectx = C.add(
            'dynamic triangle',
            scale=0.2,
            angle=left_bar_angle,
            left=5,
            top=C.scene.height - objectx_vertical_top_offset)
    else:
        objectx = C.add(
            'dynamic ball',
            scale=0.2,
            angle=left_bar_angle,
            left=5,
            top=C.scene.height - objectx_vertical_top_offset)

    # A fake bar to compute whether jar touches the left bar.
    # fake_bar_y = objectx.top if abs(angle) > 90 else objectx.bottom
    # fake_bar_scale = (fake_bar_y - bar_left.bottom) / (bar_left.top - bar_left.bottom)
    # fake_bar_left = C.add(
    #     'static bar',
    #     scale=fake_bar_scale,
    #     angle=angle,
    #     right=bar_left.right,
    #     bottom=bar_left.bottom)
    # bar_x = fake_bar_left.right if abs(angle) > 90 else fake_bar_left.left
    objectx.set_left(max(objectx.left, bar_left.right + 5))

    # ball = C.add(
    #     'dynamic ball',
    #     scale=0.08,
    #     center_x=objectx.center_x,
    #     center_y=objectx.center_y,
    #     right=0.8 * C.scene.width,
    #     bottom=0.9 * C.scene.height)

    # Create assignment.
    C.update_task(
        body1=objectx,
        body2=floor,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)
