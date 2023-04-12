import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='CartPoleMod-original',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':1},
)
register(
    id='CartPoleMod-light',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':2},
)
register(
    id='CartPoleMod-heavt',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':3},
)
register(
    id='CartPoleMod-long',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':4},
)
register(
    id='CartPoleMod-short',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':5},
)
register(
    id='CartPoleMod-soft',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':6},
)
register(
    id='CartPoleMod-strong',
    entry_point='gym_cartpolemod.envs:CartPoleModEnv',
    kwargs={'case':7},
)
