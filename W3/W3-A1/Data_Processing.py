from ucimlrepo import fetch_ucirepo

# fetch dataset
iris = fetch_ucirepo(id=53)

# data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets

# metadata
print(iris.metadata)

# variable information
print(iris.variables)

# Total number of records
print("Total number of records:", len(X))

# Total number of different flowers
print("Total number of different flowers:", y.nunique().iloc[0])

# Names of all different flowers
print("Names of different flowers:")
print(y.iloc[:, 0].unique())