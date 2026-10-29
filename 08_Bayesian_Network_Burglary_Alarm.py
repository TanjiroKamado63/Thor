# Practical 8: Bayesian Network for Burglary and Alarm
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import DiscreteBayesianNetwork

model = DiscreteBayesianNetwork([
    ("Burglary", "Alarm"),
    ("Earthquake", "Alarm"),
])

cpd_b = TabularCPD(variable="Burglary", variable_card=2, values=[[0.99], [0.01]])
cpd_e = TabularCPD(variable="Earthquake", variable_card=2, values=[[0.98], [0.02]])

# Evidence columns: [False,False], [False,True], [True,False], [True,True]
cpd_a = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[
        [0.999, 0.06, 0.71, 0.05],
        [0.001, 0.94, 0.29, 0.95],
    ],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
)

model.add_cpds(cpd_b, cpd_e, cpd_a)

inference = VariableElimination(model)
posterior = inference.query(variables=["Burglary"], evidence={"Alarm": 1})
print(posterior)
