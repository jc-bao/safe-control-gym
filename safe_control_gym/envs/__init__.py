"""Register environments.

"""
from safe_control_gym.utils.registration import register

register(id="cartpole",
         entry_point="safe_control_gym.envs.gym_control.cartpole:CartPole",
         config_entry_point="safe_control_gym.envs.gym_control:cartpole.yaml")

register(id="quadrotor",
         entry_point="safe_control_gym.envs.gym_pybullet_drones.quadrotor:Quadrotor",
         config_entry_point="safe_control_gym.envs.gym_pybullet_drones:quadrotor.yaml")

register(id="quadrotor-naive",
         entry_point="safe_control_gym.envs.gym_naive_drones.quadrotor:Quadrotor",
         config_entry_point="safe_control_gym.envs.gym_naive_drones:quadrotor.yaml")