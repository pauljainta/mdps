from mdp import MDP
import numpy as np
import math
import copy


def get_random_policy(env):
    n = env.num_states
    a = env.num_actions
    policy =  np.random.randint(0, a, size=n) 
    return policy

def action_to_string(act, UP=0, DOWN=1, LEFT=2, RIGHT=3):
    if act == UP:
        return "^"
    elif act == DOWN:
        return "v"
    elif act == LEFT:
        return "<"
    elif act == RIGHT:
        return ">"
    else:
        return NotImplementedError




def visualize_policy(policy, env):
    """
  prints the policy of the MDP using text arrows and uses a '.' for terminals
  """
    count = 0
    for r in range(env.num_rows):
        policy_row = ""
        for c in range(env.num_cols):
            if count in env.terminals:
                policy_row += ".\t"    
            else:
                policy_row += action_to_string(policy[count]) + "\t"
            count += 1
        print(policy_row)


def print_array_as_grid(array_values, env):
    """
  Prints array as a grid
  :param array_values:
  :param env:
  :return:
  """
    count = 0
    for r in range(env.num_rows):
        print_row = ""
        for c in range(env.num_cols):
            print_row += "{:.2f}\t".format(array_values[count])
            count += 1
        print(print_row)




def value_iteration(env, epsilon=0.0001):
    """
    Run value iteration to find optimal values for each state
  :param env: the MDP
  :param epsilon: numerical precision for values to determine stopping condition
  :return: the vector of optimal values for each state in the MDP 
  """
    n = env.num_states
    V = np.zeros(n)  # could also use np.zero(n)
    #TODO: implement value iteration

    return V




def extract_optimal_policy(V, env, epsilon=0.0001):
    """ 
    Perform a one step lookahead to find optimal policy
    :param V: precomputed values from value iteration
    :param env: the MDP
    :param epsilon: numerical precision for values to determine stopping condition
    :return: the optimal policy
    """
    n = env.num_states
    optimal_policy =  get_random_policy(env) 
    #TODO: Perform a one step lookahead to find optimal policy 


  
    return optimal_policy






def policy_evaluation(policy, env, epsilon):
    """
    Evalute the policy and compute values in each state when executing the policy in the mdp
    :param policy: the policy to evaluate in the mdp
    :param env: markov decision process where we evaluate the policy
    :param epsilon: numerical precision desired
    :return: values of policy under mdp
    """
    n = env.num_states
    V = np.zeros(n)  # could also use np.zero(n)
    #TODO: code up policy evaluation

    return V


def policy_iteration(env, epsilon=0.0001):
    """
    Run policy iteration to find optimal values and policy
    :param env: markov decision process where we evaluate the policy
    :param epsilon: numerical precision desired
    :return: values of policy under mdp
    """
    #start with random policy
    n = env.num_states
    a = env.num_actions
    policy =  get_random_policy(env)  # Generates random policy to start policy iteration
    # print('random policy', policy)

    policy_stable = False
    ##!!Note: this is currently an infinite loop!!##
    while not policy_stable:
        #run policy evaluation
        #TODO: implement policy_evaluation
        V = policy_evaluation(policy, env, epsilon)
       
        #TODO: run policy improvement

    
    return policy, V


