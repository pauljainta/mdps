import mdp
import mdp_utils
import numpy as np

# Create homework grid world 
grid_env = mdp.gen_simple_world() #Change this function call for part 2

# Visualize rewards
print("rewards")
mdp_utils.print_array_as_grid(grid_env.rewards, grid_env)

print("visualize a random policy")
random_pi = mdp_utils.get_random_policy(grid_env)
mdp_utils.visualize_policy(random_pi, grid_env)

print("--- value iteration ---")
V_vi = mdp_utils.value_iteration(grid_env)
print("Values from Value Iteration")
mdp_utils.print_array_as_grid(V_vi, grid_env)
opt_pi = mdp_utils.extract_optimal_policy(V_vi, grid_env)
print("Optimal Policy")
mdp_utils.visualize_policy(opt_pi, grid_env)

print("--- policy iteration ---")
policy_pi, V_pi = mdp_utils.policy_iteration(grid_env)
print("Optimal Policy")
mdp_utils.visualize_policy(policy_pi, grid_env)
print("Values from Policy Iteration")
mdp_utils.print_array_as_grid(V_pi, grid_env)