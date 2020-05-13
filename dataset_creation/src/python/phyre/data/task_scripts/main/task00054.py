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

"""Template task with a ball that should not fall into a jar."""
import phyre.creator as creator_lib

__JAR_XS = [val * 0.1 for val in range(2, 8)]
__JAR_SCALES = [val * 0.05 for val in range(5, 12)]
__BALL_YS = [val * 0.1 for val in range(6, 10)]
__BALL_RS = [val * 0.05 for val in range(1, 3)]


@creator_lib.define_task_template(
    jar_x=__JAR_XS,
    jar_scale=__JAR_SCALES,
    ball_y=__BALL_YS,
    search_params=dict(
        required_flags=['BALL:GOOD_STABLE'],
        diversify_tier='ball'
    ),
    over=[True, False],
    ball_r=__BALL_RS,
    version='3')
def build_task(C, jar_x, jar_scale, ball_y, ball_r, over):

    # shape1
    shape1 = C.add(
            'static box',
            scale=jar_scale,
            angle=90,
            left=0,
            bottom=0)

    # ramp on top of the shape
    ramp = C.add(
            'static isotriangle',
            scale=jar_scale,
            left=0,
            bottom=shape1.top)

    # Add jar.
    jar = C.add('dynamic jar',
                scale=jar_scale,
                bottom=0 ,
                left=ramp.right)

    bar = C.add('dynamic bar',
                scale=jar_scale+0.1,
                bottom=jar.top ,
                left=ramp.right)

    if jar.left < 0. or bar.right > C.scene.width:
        raise creator_lib.SkipTemplateParams


    # Add ball that hovers over the jar.
    ball = C.add('dynamic ball',
                 scale=ball_r,
                 left=ball_r* C.scene.width,
                 bottom=ramp.top)
    if ball.top > C.scene.height:
        raise creator_lib.SkipTemplateParams


    if over:
        cause_ball = C.add('dynamic ball',
                 scale=ball_r+0.05,
                 bottom=bar.top+0.2 * C.scene.height,
                 center_x=(jar.left+jar.right)/2.)
    else:
        cause_box = C.add('dynamic ball',
                 scale=ball_r+0.05,
                 bottom=bar.top+0.2 * C.scene.height,
                 center_x=(bar.right+jar.right)/2.)

    # Create assignment.
    C.update_task(body1=ball,
                  body2=jar,
                  relationships=[C.SpatialRelationship.TOUCHING],
                  over=over)
    C.set_meta(C.SolutionTier.BALL)
