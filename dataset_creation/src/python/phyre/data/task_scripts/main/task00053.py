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

"""Template task with a ball that should avoid an catapult bar to hit ground."""
import phyre.creator as creator_lib
import random
import numpy as np
import math

__catapult_WIDTHS = [val * 0.1 for val in range(3, 6)]
__catapult_YS = [val * 0.1 for val in range(2, 4)]
__catapult_XS = [val * 0.1 for val in range(2, 4)]


@creator_lib.define_task_template(
    catapult_width=__catapult_WIDTHS,
    catapult_x=__catapult_XS,
    catapult_y=__catapult_YS,
    ball_r=np.linspace(0.03, 0.09, 5),
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        excluded_flags=['BALL:TRIVIAL'],
        diversify_tier='ball'
    ),
    over=[True, False],
    max_tasks=100)

def build_task(C, catapult_width, catapult_x, catapult_y, ball_r, over):
    # Add catapult.

    fulcrum_triangle = C.add('static triangle', 
                            scale=0.2,
                            bottom =0,
                            left=catapult_x*C.scene.width) 
            

    if catapult_x + catapult_width > 1.:
        raise creator_lib.SkipTemplateParams

    left_limit = catapult_x 
    right_limit = catapult_x + catapult_width

    # multiply with width and height to get absolute values
    catapult_x *= C.scene.width
    catapult_y *= C.scene.height
    #red = color_to_id('red')

    catapult = C.add('dynamic catapult', scale=catapult_width) \
                .set_center_x(fulcrum_triangle.center_x) \
                .set_center_y(fulcrum_triangle.center_y) \
                .set_bottom(fulcrum_triangle.top) 
    
    support_bar = C.add('static bar', scale=(math.sqrt(3)*0.2)/2., left=catapult.left, bottom=0, angle=90)


    ball_throw = C.add('dynamic ball', scale=0.03, bottom =fulcrum_triangle.top) \
                 .set_center_x(catapult.center_x - (catapult.width/4.)) \


    center_ball = catapult_x + catapult.width / 2.

    ball = C.add('dynamic ball', 0.2) \
        .set_center_x(center_ball) \
        .set_bottom(0.75 * C.scene.height) \
        #print (over, catapult_x/C.scene.width + catapult_width/2.0, center_ball/C.scene.width)

    target_jar = C.add(
        'static jar',
        scale=0.2,
        right=C.scene.width,
        bottom = 0)



    # Create assignment.
    C.update_task(
        body1=ball_throw,
        body2=target_jar,
        relationships=[C.SpatialRelationship.TOUCHING],
        over=over)
    C.set_meta(C.SolutionTier.BALL)