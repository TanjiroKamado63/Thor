# Practical 6: Disease Probability using Bayes' Theorem
def calculate_disease_probability():
    prob_disease = 0.01
    prob_no_disease = 0.99
    true_positive_rate = 0.99
    false_positive_rate = 0.05

    prob_positive_test = (
        true_positive_rate * prob_disease
        + false_positive_rate * prob_no_disease
    )

    prob_disease_given_positive = (
        true_positive_rate * prob_disease
    ) / prob_positive_test

    print(f"Total probability of testing positive P(T+): {prob_positive_test:.4f}")
    print(
        "Probability of actually having the disease given a positive test "
        f"P(D|T+): {prob_disease_given_positive:.4f}"
    )
    print(f"In percentage: {prob_disease_given_positive * 100:.2f}%")


if __name__ == "__main__":
    calculate_disease_probability()
