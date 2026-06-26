import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Define an agent-based model for wealth distribution using kinetic theory
class AgentBasedWealthModel:
    def __init__(self, num_agents, initial_wealth, transaction_fraction=0.1):
        self.num_agents = num_agents
        self.wealth = np.full(num_agents, initial_wealth, dtype=np.float32)
        self.transaction_fraction = transaction_fraction

    def interact(self):
        # Randomly select two agents
        i, j = np.random.choice(self.num_agents, 2, replace=False)
        # Determine the amount to be exchanged
        delta = self.transaction_fraction * min(self.wealth[i], self.wealth[j])
        # Randomly decide the direction of the transaction
        if np.random.rand() < 0.5:
            self.wealth[i] += delta
            self.wealth[j] -= delta
        else:
            self.wealth[i] -= delta
            self.wealth[j] += delta

    def simulate(self, steps):
        for _ in range(steps):
            self.interact()

    def get_wealth_distribution(self):
        return self.wealth

# Define a PyTorch-based neural network for predicting wealth distribution
class WealthPredictor(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(WealthPredictor, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Custom dataset for training the wealth predictor
class WealthDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

if __name__ == '__main__':
    # Parameters
    num_agents = 100
    initial_wealth = 100.0
    transaction_fraction = 0.1
    simulation_steps = 10000

    # Simulate the agent-based wealth model
    model = AgentBasedWealthModel(num_agents, initial_wealth, transaction_fraction)
    model.simulate(simulation_steps)
    wealth_distribution = model.get_wealth_distribution()

    # Prepare data for training the neural network
    # Here, we use a simple example where the input is the agent index
    # and the output is the corresponding wealth
    data = np.arange(num_agents).reshape(-1, 1).astype(np.float32)
    labels = wealth_distribution.reshape(-1, 1)

    dataset = WealthDataset(data, labels)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

    # Define and train the neural network
    input_dim = 1
    hidden_dim = 32
    output_dim = 1
    predictor = WealthPredictor(input_dim, hidden_dim, output_dim)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(predictor.parameters(), lr=0.01)

    epochs = 100
    for epoch in range(epochs):
        for batch_data, batch_labels in dataloader:
            optimizer.zero_grad()
            outputs = predictor(batch_data)
            loss = criterion(outputs, batch_labels)
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')

    # Test the trained model
    test_data = torch.tensor(data, dtype=torch.float32)
    predicted_wealth = predictor(test_data).detach().numpy()

    # Print the actual and predicted wealth distributions
    print("Actual Wealth Distribution:", wealth_distribution)
    print("Predicted Wealth Distribution:", predicted_wealth.flatten())