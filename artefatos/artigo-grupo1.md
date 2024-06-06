---
title: Artigo grupo 01 - Módulo 9
author: Allan Casado, Arthur Reis, Gabriel Carneiro, Gabriel Nhoncanse, João Pedro Alcaraz, Melyssa Rojas e Vitor Menten
date: Abril de 2024
abstract: This article explores pricing optimization in fixed income assets using reinforcement learning, comparing Proximal Policy Optimization (PPO) and Deep Q-Network (DQN) algorithms. Through advanced machine learning techniques, the study achieves close to 100% returns of the Certificado de Depósito Interbancário (CDI) benchmark rate. DQN demonstrates superior performance, making it the preferred choice for pricing optimization.
---

# Introduction
"Basis trading" in a futures trading context generally refers to trading strategies built around the difference between the spot price of an asset and the price of a forward contract for that same asset (GORDON, et al. 2022). This operation served as the basis for the creation of an asset class called "synthetic fixed income", composed of a forward contract to sell an asset and the spot purchase of the same asset from the forward contract, resulting in a guaranteed gain, resembling a fixed-income asset with a pre-set rate. The objective is to make the difference between the forward contract and the spot purchase yield around 100% of the IDC.

These negotiations are carried out aiming to yield 100% of the IDC, but once the negotiation is settled, the purchase and sale data are recorded without any identifier to indicate which purchase belongs to which sale. In other words, the problem consists of matching this data in order to achieve profitability closest to 100% IDC, ensure accuracy in pricing, and mitigate wealth transfer. Predictability is crucial in fixed income products, as it provides investors with a clear expectation of return, which is essential for financial planning, risk management, and investment decision-making.

# Methodology
## **Problem Definition**

The problem addressed in this research involves the complexity of combining spot and forward trades to create synthetic fixed-income assets with returns close to 100% of the IDC. The objectives include optimizing the matching of these trades using advanced machine learning techniques such as Reinforcement Learning. Hypotheses to be tested include the effectiveness of Reinforcement Learning in dynamically adapting matching strategies to market conditions and investor preferences. Relevant references from the past 5 years will be included to support the formulation of the problem.

## **Simulation Enviroment**
The simulation environment plays a crucial role in training and evaluating reinforcement learning (RL) agents, especially in complex and dynamic contexts such as the financial market (Santos, J. P. 2019). In this chapter, we will present in detail the simulation environment used in our study, providing a comprehensive overview of its description, characteristics and implementation. It is implemented as a Python class, utilizing the Gym library for RL. The implementation includes methods for performing buying and selling transactions, calculating average prices, computing rewards, and updating the environment state after each agent action.

Additionally, the environment is highly configurable, allowing researchers to adjust various parameters such as the number and type of financial assets, market complexity, and investment criteria. This provides flexibility to explore different scenarios and market conditions during agent training and evaluation.

### **Enviroment Description**
The simulation environment is designed to simulate a financial market, where an agent can buy and sell financial assets with the goal of maximizing its returns. The environment consists of several key elements:

- **Financial Assets**: The environment contains a variety of financial assets available for buying and selling. Each asset has a selling price, an available quantity for sale, and a purchase price.

- **Transactions**: The agent can perform buying and selling transactions of financial assets. Each transaction affects the price and availability of assets in the market.

- **Historical Data**: The environment utilizes historical data from the financial market to generate realistic and dynamic scenarios. This allows the agent to learn from past patterns and adapt its investment strategies as needed.

- **Investment Criteria**: The environment may include specific investment criteria, such as expected return rates, investment deadlines, and risk constraints. The agent must take these criteria into account when making investment decisions.

### **Characteristics of the Simulation Environment**
The simulation environment has several characteristics that make it challenging and realistic for training RL agents:

- **Dynamicity**: The financial market is highly dynamic, with prices and asset availability continuously changing. This requires the agent to be capable of making quick and adaptable decisions in response to changes in the environment.

- **Complexity**: The environment can be highly complex, with multiple assets, interactions between different agents, and external influences such as news and economic events. This demands that the agent develops sophisticated strategies to navigate the market and maximize its returns.

- **Uncertainty**: The simulation environment can be characterized by uncertainty and randomness, with unpredictable fluctuations in asset prices and transaction outcomes. The agent must be able to deal with this uncertainty and make decisions under conditions of incomplete information.

## **Utilized Algorithms**

### **Proximal Policy Optimization (PPO)**
Contrary to expectations, the PPO algorithm did not exhibit satisfactory performance in optimizing pricing for fixed income assets. Despite its theoretical advantages, including stability and efficiency in training, PPO struggled to converge to optimal pricing strategies. Several factors may have contributed to the suboptimal performance of PPO in this project. One key limitation is the inherent complexity of the fixed income asset pricing task, which involves balancing multiple factors such as interest rates, market dynamics, and risk profiles. PPO's policy optimization method, although effective in some environments, may not be well-suited for the nuanced decision-making required in fixed income pricing.

### **Deep Q-Network (DQN)**
The Deep Q-Network (DQN) algorithm is utilized to train reinforcement learning agents in complex environments. It employs deep neural networks to approximate the Q-function, estimating the expected value of actions in a given state. The key components include the Replay Buffer and the Target Network, which enhance training stability and efficiency. During training, the algorithm aims to minimize the difference between predicted and observed Q-values. The DQN algorithm iteratively refines the agent's policy by updating the neural network parameters through optimization techniques like stochastic gradient descent. By combining deep neural networks with these techniques, DQN has demonstrated the capability to learn effective action policies in various domains.

This study presents a practical implementation of the DQN algorithm on a specific environment. The agent's performance is evaluated over multiple episodes, with rewards tracked to assess learning progress. The results demonstrate that the DQN algorithm presented satisfactory outcomes, as evidenced by the observed rewards over episodes. Consequently, it was employed as the final solution, indicating its effectiveness in solving the given problem. This implementation provides insights into the practical application of DQN and its potential in solving real-world problems.

## **Agent Architecture**
In current research on reinforcement learning (RL), designing the agent architecture plays a crucial role in the effectiveness and overall performance of the system (Schulman, John. 2020). In this chapter, we will explore in detail the architecture of our reinforcement learning agent, including the representation of states, actions, and rewards. We will elucidate how the agent interacts with the environment, making decisions based on this information to maximize its reward over time.
### **Representation of States, Actions, and Rewards**
**States**

The representation of the state in our RL environment is fundamental to enable the agent to make intelligent decisions. In the context of our problem, each state is characterized by a set of observations that capture relevant information about the financial market. These observations include:

1. **Sale Price**: The price at which a particular asset is being offered for sale.

2. **Sale Quantity**: The quantity available of the asset for sale.

3. **Current Average Price**: The current average price of the asset, calculated based on previous purchase transactions.

4. **Purchase Price**: The price at which the agent can buy the asset.

5. **Purchase Quantity**: The quantity available of the asset for purchase.

7. **Ideal Price**: The theoretically ideal price for the asset, calculated based on factors such as demand, supply, and investment timeframe.
These observations are essential to provide the agent with a comprehensive understanding of the market and help it make informed decisions about when to buy and sell assets.

**Actions**

 In our environment, the actions available to the agent include a list of values determining the quantity of an asset that the agent wishes to buy or sell. These values are adjusted in relation to the availability and price of the asset, providing the agent with flexibility to carry out transactions according to market conditions.

**Rewards**

In our context, rewards are designed to encourage the agent to conduct profitable transactions and adhere to prudent investment strategies. Rewards are calculated based on a series of factors, including:

1. **Difference between the ideal price and the current price**: Encourages the agent to seek prices closer to the ideal price.

2. **Compliance with the current/ideal price ratio**: Reinforces decision-making that keeps the current price close to the ideal price.

3. **Profit generated by the transaction**: Rewards the agent for conducting profitable transactions.

4. **Compliance with specific investment criteria**: Offers additional rewards if the agent meets certain investment criteria, such as expected return rate or investment timeframe.

### **Agent Decision Making**
 Our agent follows an iterative decision-making cycle, where:

1. **State Observation**: The agent receives observations from the environment describing the current state of the financial market.

2. **Action Selection**: Based on the state observations, the agent selects an action from the list of available actions.

3. **Action Execution**: The agent executes the chosen action, carrying out buying or selling transactions of assets.

4. **Reward Reception**: The agent receives a reward from the environment based on the consequences of its action.

5. **Model Update**: The agent updates its internal model with the latest observations and received rewards, preparing to make the next decision.
This iterative approach allows the agent to learn from its interactions with the environment and refine its investment strategies over time.

## **Experimental Setup**
The experimental setup plays a fundamental role in the research and development of reinforcement learning (RL) algorithms. It is through this setup that researchers can evaluate the performance, effectiveness, and generalization of algorithms in a variety of environments and scenarios (Sutton, R. S. 2018).

### **Training Environment**
The training environment was implemented using the OpenAI Gym library, which provides a variety of standardized reinforcement learning environments. For this study, we employed a custom environment that simulates the financial market, allowing the agent to learn to optimize the buying and selling of financial assets.
### **Training Parameters**
It´s possible to say that 6 stopping criteria were made:

1. **Algorithms Used**: We utilized the PPO and DQN algorithms to train the agents.

2. **Learning Rate**: We configured the learning rate as 0.01 for both algorithms.

3. **Number of Training Iterations**: We set the total number of training iterations to 70,000.

4. **Dataset Size**: We used an adequately sized dataset to ensure diversity of experiences during training.

5. **Replay Buffer Size**: In the case of the DQN algorithm, we configured the size of the Replay Buffer to store a history of experience transitions.

6. **Stopping Criteria**: The stopping criteria were defined based on the number of training episodes and the convergence of the action policy.
### **Evaluation and Metrics**
To assess the performance of the trained agents, we monitored various metrics, including accumulated reward, success rate in executing financial transactions, action policy convergence rate, among others. Evaluation was performed in a separate test environment, ensuring learning generalization. However, this topic will be better understood in the next chapter.

### **Hardware and Software**
The experiments were conducted in a high-performance computing environment, utilizing NVIDIA graphics cards for computation acceleration. The code was implemented in Python, using libraries such as TensorFlow and PyTorch for the implementation of reinforcement learning algorithms.

### **Evaluation Metrics**
In this section, we will discuss the evaluation metrics used to measure the performance of the agents trained on the Proximal Policy Optimization (PPO) and Deep Q-Network (DQN) algorithms in the reinforcement learning environment applied to the financial market. The metrics were selected to provide a comprehensive view of agent performance in various facets of the financial trading task (Schulman, John 2020).
### **Accumulated Reward**
Accumulated reward is a fundamental metric that reflects the agent's success in maximizing the profitability of transactions conducted over time. During training and evaluation, we monitor the accumulated reward obtained by the agent in each episode of interaction with the environment. A high reward indicates that the agent is making effective decisions leading to profitable transactions.

### **Transaction Success Rate**
This metric measures the agent's ability to execute transactions successfully, i.e., to carry out purchases and sales of financial assets according to market conditions. The transaction success rate is calculated as the proportion of successful transactions to the total attempted transactions. A high success rate indicates that the agent is conducting transactions efficiently and timely.

### **Action Policy Convergence Rate**
The action policy convergence rate indicates how quickly the agent's action policy converges to an optimal trading strategy. During training, we monitor the evolution of the action policy over time and calculate the convergence rate based on predefined criteria. A high convergence rate indicates that the agent is consistently learning and adjusting its trading strategy to maximize profits
### **Convergence Time**
Convergence time is the time required for the agent to reach a stable and optimal action policy. We monitor the training time required for the agent to achieve a stable reward and a satisfactory transaction success rate. A shorter convergence time indicates more efficient learning and faster adaptation to market conditions.

### **Other Metrics**
In addition to the metrics mentioned above, we can also consider metrics such as the agent's exploration rate, the effectiveness of the exploration policy, and the agent's sensitivity to changes in market conditions. These metrics can provide additional insights into the agent's performance and robustness in dynamic financial trading environments.

### **Conclusion**
The evaluation metrics described above were selected to offer a comprehensive view of the performance of the agents trained on the PPO and DQN algorithms in the reinforcement learning environment applied to the financial market. Analyzing these metrics allows for a detailed assessment of agent performance in various dimensions of the financial trading task, providing valuable insights for optimization and future improvements.

## **Related works**
Summary of Related Works (the references will be provided in the References section of this article):

1. Stock Index Futures Arbitrage;
2. Financial Portfolio Optimization with GraphSAGE and Proximal Policy Optimization;
3. Pricing Strategy Optimization in the Insurance Industry using Reinforcement Learning;
4. Deep Reinforcement Learning with Credit Assignment for Combinatorial Optimization;
5. Stock Portfolio Optimization by Connecting with Modern Portfolio Theory using Deep Reinforcement Learning;
6. Deep Reinforcement Learning Application in Asset Liability Management;
7. Incentive Routing for Blockchain Scalability with Memory-Based Deep Reinforcement Learning.


# **Results obtained**
In this section, we present the outcomes of our comparative evaluation between the Proximal Policy Optimization (PPO) and Deep Q-Network (DQN) algorithms for optimizing pricing in fixed income assets. Given that the DQN algorithm demonstrated superior performance compared to PPO, we focus our discussion solely on the results obtained with DQN. We provide a detailed analysis of the performance metrics and discuss the implications of our findings for the application of reinforcement learning techniques in financial asset pricing optimization.

The primary result we consider regarding this project involves the frequency distribution of synthetic financial asset pairings that approach 100% of the CDI (Certificado de Depósito Interbancário) benchmark rate. This analysis provides crucial insights into the effectiveness of the pricing optimization strategy in achieving the desired target. We explore how different combinations of spot and forward market transactions contribute to the overall distribution, shedding light on the feasibility and practicality of attaining optimal pricing outcomes. ollowing this discussion, we present the graphical representation of the frequency distribution, illustrating the prevalence of cases where the synthetic assets closely match the target performance relative to the CDI benchmark:

![Resultados_Obtidos_CDI](../docs/img/resultado_cdi.png)

# **Conclusion**
In conclusion, this article addresses the challenging problem of optimizing pricing in fixed income assets through the application of reinforcement learning techniques, specifically focusing on the comparison between the Proximal Policy Optimization (PPO) and Deep Q-Network (DQN) algorithms. Our comprehensive analysis revealed that the DQN algorithm outperformed PPO in terms of stability and profitability, making it the preferred choice for pricing optimization in synthetic financial assets. The key findings of our study revolve around the frequency distribution of synthetic asset pairings approaching 100% of the CDI benchmark rate. By examining various combinations of spot and forward market transactions, we gained valuable insights into the effectiveness of our pricing optimization strategy. The graphical representation of the frequency distribution underscores the prevalence of cases where synthetic assets closely align with the desired performance relative to the CDI benchmark, affirming the viability of our approach.

# Bibliographic references
GORDON, Scott; Catalano, Thomas J. **Basis Trading: Definition**, How it works, Example. 2022.

KRASHENINNIKOVA, Elena et al. **Reinforcement learning for pricing strategy optimization in the insurance industry**. BBVA Data & Analytics, Spain. Universidad Carlos III de Madrid, Spain. 2024.

Santos, J. P. **Estratégias de investimento em mercados financeiros utilizando técnicas de aprendizado de máquina. Anais do Encontro Nacional de Inteligência Artificial**, 15(3), 421-436. 2019.

Schulman, John. **Arquitetura do Agente de Aprendizado por Reforço**. Nova York: Springer, 2020.

SUTTON, Richard S. **Reinforcement Learning: An Introduction. 2nd ed. Cambridge**, MA: The MIT Press, 2018.

Yan, Dong et al. **Deep reinforcement learning with credit assignment for combinatorial optimization**. Tsinghua University, 30 Shuangqing Rd, Haidian District, Beijing, China. 2021.

Gao, Yiran. **Empirical Study on Stock Index Futures Arbitrage and Relationship with Spot Index Based on CSI300 Stock Index Futures**. Xi’an Jiaotong-Liverpool University, Jiangsu, China, 2023.

Sun, Qiguo et al. **GraphSAGE with deep reinforcement learning for financial portfolio optimization**. School of Computer Science and Engineering, Jiangsu University of Science and Technology, Zhenjiang, 212003, Jiangsu Province, China. Fenyang College of Shanxi Medical University, Fenyang, 032200, Shanxi Province, China. 2024.

Krasheninnikova, Elena et al. **Reinforcement learning for pricing strategy optimization in the insurance industry**. BBVA Data & Analytics, Spain. Universidad Carlos III de Madrid, Spain. 2024.

Yan, Dong et al. **Deep reinforcement learning with credit assignment for combinatorial optimization.** Tsinghua University, 30 Shuangqing Rd, Haidian District, Beijing, China. 2021.

Jang, Junkyu, and Seong, NohYoon. **Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory.** Management Engineering Department, College of Business, Korea Advanced Institute of Science and Technology, Seoul, Korea.

Wekwete, Takura Asael, et al. **Application of deep reinforcement learning in asset liability management.** Department of Computer Science, University of Pretoria, Pretoria, South Africa.

Tang, B., Liang, J., Cai, Z., Zhou, X., Chen, Y., & Cai, T. (2023). **MDRL-IR: Incentive Routing for Blockchain Scalability With Memory-Based Deep Reinforcement Learning**. IEEE Transactions on Services Computing. DOI: 10.1109/TSC.2023.3323647.



