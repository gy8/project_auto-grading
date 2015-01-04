"""     @author:        Guang Yang
        @mktime:        9/27/2014
        @description:   solution bank for multiple choice and data analysis
"""


import sqlite3 as lite


def new_solutions_db():
    """ initializes a sqlite database called 'solutions.db', where solutions
    for all 4 labs are to be stored in 3 tables: mc, ts and da.
    - documentation only, executed in commandline sqlite -

    Schema:
        MC (multiple choice):
            lab_num (int):             1,2,3,4
            question_num (int):         1,2,3,4,5,...
            error_name (text):          'a','e',...
            feedback (text):            "The correct answer is A Teehee"

        TS (test selection):
            lab number (int):           1,2,3,4
            question number (int):      1,2,3,4,5,...
            error_name (text):           'a','e',...
            feedback (text):             "The correct answer is A Teehee"

        DA (data analysis):
            lab_num (int):             1,2,3,4
            question_num (int):         1,2,3,4,5,...
            part_name (text):           'a','c',...
            error_name (text):          'a','e',...
            feedback (text):            "The correct answer is A Teehee"
            points_off (int):           1,2,3,4,5,...
    """
    pass


def new_grades_db():
    """ initializes a sqlite database called 'grades.db', where grades for each
    student is stored
    - documentation only, executed in commandline sqlite -

    Schema:
        Grades:
            section number (int)
            lab number (int)
            student name (str)
            student score (int)
    """
    pass


def solution_mult_choice_lab1():
    """ solution bank for multiple choices (lab 1)- data are stored in a
    tuple where the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab1 q1
    mc_sol.append((1, 1, 'a', "The correct answer is E. Remember that "
                   "intervals have different lengths"))
    mc_sol.append((1, 1, "b", "The correct answer is E. Dichotomous variables "
                   "are nomial with only categories or levels, which is not "
                   "the case here"))
    mc_sol.append((1, 1, "c", "The correct answer is E. Nominal variables "
                   "do not impose order, however here there is indeed order "
                   "from less to more"))
    mc_sol.append((1, 1, "d", "The correct answer is E. Since ratio "
                   "variables are also continuous, it can't be the case here"))

    # lab1 q2
    mc_sol.append((1, 2, "b", "The correct answer is A. Dichotomous is binary"
                   ", not an interval variable"))
    mc_sol.append((1, 2, "c", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "d", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "e", "The correct answer is A. It's not clear what's "
                   "conceptual vs operational"))

    # lab1 q3
    mc_sol.append((1, 3, "a", "The correct answer is D. Not true - std "
                   "indeed gets 'stretched' by outliers"))
    mc_sol.append((1, 3, "b", "The correct answer is D. This was a little "
                   "tricky - the problem here is the use of 'any population'. "
                   "Let's demonstrate this by a counterexample. Say we have "
                   "two distributions, X which is normal distribution with "
                   "mean mu and standard deviation sigma, and Y which is a "
                   "constant distribution over the support of a singleton 5. "
                   "For X, it's clear that sampling a point from a normal "
                   "distribution has about 68%% chance of falling within one "
                   "standard deviation of the mean. However, since Y is a "
                   "singleton, the mean is 5 and variance is 0. As a result, "
                   "The chance of your sample falling within one standard "
                   "deviation of the mean is 100%%."))
    mc_sol.append((1, 3, "c", "The correct answer is D. Take the constant "
                   "to be 0 and it's very clear this is wrong"))

    # lab1 q4
    mc_sol.append((1, 4, "a", "The correct answer is B. This answer doesn't "
                   "make sense as there is no quota"))
    mc_sol.append((1, 4, "c", "The correct answer is B. Where is the social "
                   "network?"))
    mc_sol.append((1, 4, "d", "The correct answer is B. You need "
                   "probabilities to select clusters"))
    mc_sol.append((1, 4, "e", "The correct answer is B. But the prompt said "
                   "random"))
    mc_sol.append((1, 4, "f", "The correct answer is B. What's systematic "
                   "about it?"))

    # lab1 q5
    mc_sol.append((1, 5, "a", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "b", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "d", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))

    # lab1 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "This is a known fact, CLT is more specific."))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # lab1 q7
    mc_sol.append((1, 7, "a", "The correct answer is F. "
                   "Variance should actually stay constant with sample size"))
    mc_sol.append((1, 7, "b", "The correct answer is F. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "c", "The correct answer is F. "
                   "Notice that this is the distribution of the variable, "
                   "not the statistic. Therefore, we expect the standard "
                   "deviation to stay roughly constant with sample size, "
                   "not decrease to zero"))
    mc_sol.append((1, 7, "d", "The correct answer is F. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "e", "The correct answer is F. "
                   "That's not what central limit theorem tells us"))

    # lab1 q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # lab1 q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult_choice_lab2():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab2 q1
    mc_sol.append((2, 1, "b", "The correct answer is A. "
                   "Bar graph is simple and adequately captures the "
                   "information about different religious affliations"))
    mc_sol.append((2, 1, "c", "The correct answer is A. "
                   "Bar graph is simple and adequately captures the "
                   "information about different religious affliations"))
    mc_sol.append((2, 1, "d", "The correct answer is A. "
                   "Bar graph is simple and adequately captures the "
                   "information about different religious affliations"))
    mc_sol.append((2, 1, "e", "The correct answer is A. "
                   "Line charts show how data change over intervals of the "
                   "same unit of measurement (often time). Since the question "
                   "makes no mention of how their religious affiliations "
                   "change over time, we cannot use line charts"))
    mc_sol.append((2, 1, "f", "The correct answer is A. "
                   "Line charts show how data change over intervals of the "
                   "same unit of measurement (often time). Since the question "
                   "makes no mention of how their religious affiliations "
                   "change over time, we cannot use line charts"))

    # lab2 q2
    mc_sol.append((2, 2, "a", "The correct answer is C. "
                   "The null hypothesis assumes the number of song names "
                   "the student can recall is exactly 10. The alternative "
                   "hypothesis (the claim) is that the number of song names "
                   "the students can recall is greater than 10."))
    mc_sol.append((2, 2, "b", "The correct answer is C. "
                   "The null hypothesis assumes the number of song names "
                   "the student can recall is exactly 10. The alternative "
                   "hypothesis (the claim) is that the number of song names "
                   "the students can recall is greater than 10."))
    mc_sol.append((2, 2, "d", "The correct answer is C. "
                   "The null hypothesis assumes the number of song names "
                   "the student can recall is exactly 10. The alternative "
                   "hypothesis (the claim) is that the number of song names "
                   "the students can recall is greater than 10."))

    # lab2 q3
    mc_sol.append((2, 3, "a", "The correct answer is F. "
                   "Here we are reminded that while p-value is the statistical "
                   "significance, it bears no meaning on the practical "
                   "significance of the experiment (the effect size). Further "
                   "notice that the alpha is the threshold value that we "
                   "measure the p-value against and since we are not told "
                   "explicitly whether we were successful in rejecting the "
                   "null hypothesis, we do not know what alpha was set for "
                   "this experiment."))
    mc_sol.append((2, 3, "b", "The correct answer is F. "
                   "Here we are reminded that while p-value is the statistical "
                   "significance, it bears no meaning on the practical "
                   "significance of the experiment (the effect size). Further "
                   "notice that the alpha is the threshold value that we "
                   "measure the p-value against and since we are not told "
                   "explicitly whether we were successful in rejecting the "
                   "null hypothesis, we do not know what alpha was set for "
                   "this experiment."))
    mc_sol.append((2, 3, "c", "The correct answer is F. "
                   "Here we are reminded that while p-value is the statistical "
                   "significance, it bears no meaning on the practical "
                   "significance of the experiment (the effect size). Further "
                   "notice that the alpha is the threshold value that we "
                   "measure the p-value against and since we are not told "
                   "explicitly whether we were successful in rejecting the "
                   "null hypothesis, we do not know what alpha was set for "
                   "this experiment."))
    mc_sol.append((2, 3, "d", "The correct answer is F. "
                   "Here we are reminded that while p-value is the statistical "
                   "significance, it bears no meaning on the practical "
                   "significance of the experiment (the effect size). Further "
                   "notice that the alpha is the threshold value that we "
                   "measure the p-value against and since we are not told "
                   "explicitly whether we were successful in rejecting the "
                   "null hypothesis, we do not know what alpha was set for "
                   "this experiment."))
    mc_sol.append((2, 3, "e", "The correct answer is F. "
                   "Here we are reminded that while p-value is the statistical "
                   "significance, it bears no meaning on the practical "
                   "significance of the experiment (the effect size). Further "
                   "notice that the alpha is the threshold value that we "
                   "measure the p-value against and since we are not told "
                   "explicitly whether we were successful in rejecting the "
                   "null hypothesis, we do not know what alpha was set for "
                   "this experiment."))

    # lab2 q4
    mc_sol.append((2, 4, "a", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))
    mc_sol.append((2, 4, "b", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))
    mc_sol.append((2, 4, "c", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))
    mc_sol.append((2, 4, "d", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))
    mc_sol.append((2, 4, "f", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))
    mc_sol.append((2, 4, "g", "Correct answer is E. "
                   "First the possibility of a type II error will go up: "
                   "false negatives are more likely to occur if we narrow "
                   "the significance region. Second, the statistical power "
                   "will go down: recall that the power of a statistical test "
                   "is the probability of rejecting a null hypothesis given "
                   "the null hypothesis is false. Since type II error (beta) "
                   "gets bigger, power = 1-beta gets smaller."))

    # lab2 q5
    mc_sol.append((2, 5, "a", "The correct answer is E. "
                   "Notice that since the distribution is skewed to the left "
                   "- thus to make it more normal, one way is to “stretch” out "
                   "the right tail by raising the variable to a power > 1. "
                   "For example, let’s say the mu is 10, think two points 8 "
                   "and 12. if we multiply both by 10, the new points 80 and "
                   "120 will remain the same distance from the new mean, 100. "
                   "However, if we raise these points to the second power, the "
                   "new points are 64 and 144, notice 144 is now further away "
                   "from the mean."))
    mc_sol.append((2, 5, "b", "The correct answer is E. "
                   "Notice that since the distribution is skewed to the left "
                   "- thus to make it more normal, one way is to “stretch” out "
                   "the right tail by raising the variable to a power > 1. "
                   "For example, let’s say the mu is 10, think two points 8 "
                   "and 12. if we multiply both by 10, the new points 80 and "
                   "120 will remain the same distance from the new mean, 100. "
                   "However, if we raise these points to the second power, the "
                   "new points are 64 and 144, notice 144 is now further away "
                   "from the mean."))
    mc_sol.append((2, 5, "c", "The correct answer is E. "
                   "Notice that since the distribution is skewed to the left "
                   "- thus to make it more normal, one way is to “stretch” out "
                   "the right tail by raising the variable to a power > 1. "
                   "For example, let’s say the mu is 10, think two points 8 "
                   "and 12. if we multiply both by 10, the new points 80 and "
                   "120 will remain the same distance from the new mean, 100. "
                   "However, if we raise these points to the second power, the "
                   "new points are 64 and 144, notice 144 is now further away "
                   "from the mean."))
    mc_sol.append((2, 5, "d", "The correct answer is E. "
                   "Notice that since the distribution is skewed to the left "
                   "- thus to make it more normal, one way is to “stretch” out "
                   "the right tail by raising the variable to a power > 1. "
                   "For example, let’s say the mu is 10, think two points 8 "
                   "and 12. if we multiply both by 10, the new points 80 and "
                   "120 will remain the same distance from the new mean, 100. "
                   "However, if we raise these points to the second power, the "
                   "new points are 64 and 144, notice 144 is now further away "
                   "from the mean."))
    mc_sol.append((2, 5, "f", "The correct answer is E. "
                   "Notice that since the distribution is skewed to the left "
                   "- thus to make it more normal, one way is to “stretch” out "
                   "the right tail by raising the variable to a power > 1. "
                   "For example, let’s say the mu is 10, think two points 8 "
                   "and 12. if we multiply both by 10, the new points 80 and "
                   "120 will remain the same distance from the new mean, 100. "
                   "However, if we raise these points to the second power, the "
                   "new points are 64 and 144, notice 144 is now further away "
                   "from the mean."))

    # lab2 q6
    mc_sol.append((2, 6, "a", "The correct answer is B. "
                   "Remember the null hypothesis cannot be just anything - "
                   "it is a statement of no effect or no difference."))
    mc_sol.append((2, 6, "c", "The correct answer is B. "
                   "Remember the null hypothesis cannot be just anything - "
                   "it is a statement of no effect or no difference."))
    mc_sol.append((2, 6, "d", "The correct answer is B. "
                   "Remember the null hypothesis cannot be just anything - "
                   "it is a statement of no effect or no difference."))

    # lab2 q7
    mc_sol.append((2, 7, "a", "The correct answer is D. "
                   "I think the key here is that we are using a frequentist "
                   "(instead of bayesian) statistical test. In this case, we "
                   "are asking about the probability of data given hypothesis, "
                   "rather than probability of hypothesis given data as in the "
                   "bayesian case."))
    mc_sol.append((2, 7, "b", "The correct answer is D. "
                   "I think the key here is that we are using a frequentist "
                   "(instead of bayesian) statistical test. In this case, we "
                   "are asking about the probability of data given hypothesis, "
                   "rather than probability of hypothesis given data as in the "
                   "bayesian case."))
    mc_sol.append((2, 7, "c", "The correct answer is D. "
                   "I think the key here is that we are using a frequentist "
                   "(instead of bayesian) statistical test. In this case, we "
                   "are asking about the probability of data given hypothesis, "
                   "rather than probability of hypothesis given data as in the "
                   "bayesian case. Without more information we cannot say "
                   "anything about causality"))

    # lab2 q8
    mc_sol.append((2, 8, "a", "The correct answer is C. "
                   "The logic behind using hypothesis testing is to set up "
                   "a null hypothesis (that is likely to be false) and try to "
                   "reject it, where more samples potentially lead to higher "
                   "statistical significance. In this case, the 20 student "
                   "study is a quite small sample size. As a result, if we are "
                   "using hypothesis testing correctly and indeed picked a "
                   "null hypothesis that is presumably false, the p-value is "
                   "likely to decrease (hence more statistically significant "
                   "as we collect more sample"))
    mc_sol.append((2, 8, "b", "The correct answer is C. "
                   "The logic behind using hypothesis testing is to set up "
                   "a null hypothesis (that is likely to be false) and try to "
                   "reject it, where more samples potentially lead to higher "
                   "statistical significance. In this case, the 20 student "
                   "study is a quite small sample size. As a result, if we are "
                   "using hypothesis testing correctly and indeed picked a "
                   "null hypothesis that is presumably false, the p-value is "
                   "likely to decrease (hence more statistically significant "
                   "as we collect more sample"))
    mc_sol.append((2, 8, "d", "The correct answer is C. "
                   "The logic behind using hypothesis testing is to set up "
                   "a null hypothesis (that is likely to be false) and try to "
                   "reject it, where more samples potentially lead to higher "
                   "statistical significance. In this case, the 20 student "
                   "study is a quite small sample size. As a result, if we are "
                   "using hypothesis testing correctly and indeed picked a "
                   "null hypothesis that is presumably false, the p-value is "
                   "likely to decrease (hence more statistically significant "
                   "as we collect more sample"))
    mc_sol.append((2, 8, "e", "The correct answer is C. "
                   "The logic behind using hypothesis testing is to set up "
                   "a null hypothesis (that is likely to be false) and try to "
                   "reject it, where more samples potentially lead to higher "
                   "statistical significance. In this case, the 20 student "
                   "study is a quite small sample size. As a result, if we are "
                   "using hypothesis testing correctly and indeed picked a "
                   "null hypothesis that is presumably false, the p-value is "
                   "likely to decrease (hence more statistically significant "
                   "as we collect more sample"))
    mc_sol.append((2, 8, "f", "The correct answer is C. "
                   "The logic behind using hypothesis testing is to set up "
                   "a null hypothesis (that is likely to be false) and try to "
                   "reject it, where more samples potentially lead to higher "
                   "statistical significance. In this case, the 20 student "
                   "study is a quite small sample size. As a result, if we are "
                   "using hypothesis testing correctly and indeed picked a "
                   "null hypothesis that is presumably false, the p-value is "
                   "likely to decrease (hence more statistically significant "
                   "as we collect more sample"))

    # lab2 q9
    mc_sol.append((2, 9, "a", "The correct answer is D. "
                   "The combination of 1) all participants live in the same "
                   "building (and presumably talk to each other everyday), 2) "
                   "participants have 3 months to complete the experiment, 3) "
                   "the experiment is fixed for everyone, and "
                   "4) participants are rewarded with gift cards for correct "
                   "recall, is highly problematic. Specifically we can easily "
                   "imagine the situation where after participant A completes "
                   "the experiement, he tells his buddy, participant B, about "
                   "the correct solution so participant B can take hours to "
                   "memorize the ingredients and dramatically increase his "
                   "chance of correct recall (motivated by the gift card). "
                   "This would be a direct violation of independence of "
                   "observations assumption. "))
    mc_sol.append((2, 9, "b", "The correct answer is D. "
                   "The combination of 1) all participants live in the same "
                   "building (and presumably talk to each other everyday), 2) "
                   "participants have 3 months to complete the experiment, 3) "
                   "the experiment is fixed for everyone, and "
                   "4) participants are rewarded with gift cards for correct "
                   "recall, is highly problematic. Specifically we can easily "
                   "imagine the situation where after participant A completes "
                   "the experiement, he tells his buddy, participant B, about "
                   "the correct solution so participant B can take hours to "
                   "memorize the ingredients and dramatically increase his "
                   "chance of correct recall (motivated by the gift card). "
                   "This would be a direct violation of independence of "
                   "observations assumption. "))
    mc_sol.append((2, 9, "c", "The correct answer is D. "
                   "The combination of 1) all participants live in the same "
                   "building (and presumably talk to each other everyday), 2) "
                   "participants have 3 months to complete the experiment, 3) "
                   "the experiment is fixed for everyone, and "
                   "4) participants are rewarded with gift cards for correct "
                   "recall, is highly problematic. Specifically we can easily "
                   "imagine the situation where after participant A completes "
                   "the experiement, he tells his buddy, participant B, about "
                   "the correct solution so participant B can take hours to "
                   "memorize the ingredients and dramatically increase his "
                   "chance of correct recall (motivated by the gift card). "
                   "This would be a direct violation of independence of "
                   "observations assumption. "))
    mc_sol.append((2, 9, "e", "The correct answer is D. "
                   "The combination of 1) all participants live in the same "
                   "building (and presumably talk to each other everyday), 2) "
                   "participants have 3 months to complete the experiment, 3) "
                   "the experiment is fixed for everyone, and "
                   "4) participants are rewarded with gift cards for correct "
                   "recall, is highly problematic. Specifically we can easily "
                   "imagine the situation where after participant A completes "
                   "the experiement, he tells his buddy, participant B, about "
                   "the correct solution so participant B can take hours to "
                   "memorize the ingredients and dramatically increase his "
                   "chance of correct recall (motivated by the gift card). "
                   "This would be a direct violation of independence of "
                   "observations assumption. "))

    # lab2 q10
    mc_sol.append((2, 10, "a", "The correct answer is F. "
                   "The key here is that the question asked what MUST be true, "
                   "which is a very very strong statement. First of all, it is "
                   "not at all clear if either Steve or Marth committed a Type "
                   "1 or Type 2 error, for we are not given this information. "
                   "Similarly, statistical power depends on the probability "
                   "the test correct rejects the null when the null is false, "
                   "which again we simply do not know. Lastly, Steve's results "
                   "are based on experiment done on a group of students taking "
                   "the same class, which is highly unlikely to generalize to "
                   "the US population."))
    mc_sol.append((2, 10, "b", "The correct answer is F. "
                   "The key here is that the question asked what MUST be true, "
                   "which is a very very strong statement. First of all, it is "
                   "not at all clear if either Steve or Marth committed a Type "
                   "1 or Type 2 error, for we are not given this information. "
                   "Similarly, statistical power depends on the probability "
                   "the test correct rejects the null when the null is false, "
                   "which again we simply do not know. Lastly, Steve's results "
                   "are based on experiment done on a group of students taking "
                   "the same class, which is highly unlikely to generalize to "
                   "the US population."))
    mc_sol.append((2, 10, "c", "The correct answer is F. "
                   "The key here is that the question asked what MUST be true, "
                   "which is a very very strong statement. First of all, it is "
                   "not at all clear if either Steve or Marth committed a Type "
                   "1 or Type 2 error, for we are not given this information. "
                   "Similarly, statistical power depends on the probability "
                   "the test correct rejects the null when the null is false, "
                   "which again we simply do not know. Lastly, Steve's results "
                   "are based on experiment done on a group of students taking "
                   "the same class, which is highly unlikely to generalize to "
                   "the US population."))
    mc_sol.append((2, 10, "d", "The correct answer is F. "
                   "The key here is that the question asked what MUST be true, "
                   "which is a very very strong statement. First of all, it is "
                   "not at all clear if either Steve or Marth committed a Type "
                   "1 or Type 2 error, for we are not given this information. "
                   "Similarly, statistical power depends on the probability "
                   "the test correct rejects the null when the null is false, "
                   "which again we simply do not know. Lastly, Steve's results "
                   "are based on experiment done on a group of students taking "
                   "the same class, which is highly unlikely to generalize to "
                   "the US population."))
    mc_sol.append((2, 10, "e", "The correct answer is F. "
                   "The key here is that the question asked what MUST be true, "
                   "which is a very very strong statement. First of all, it is "
                   "not at all clear if either Steve or Marth committed a Type "
                   "1 or Type 2 error, for we are not given this information. "
                   "Similarly, statistical power depends on the probability "
                   "the test correct rejects the null when the null is false, "
                   "which again we simply do not know. Lastly, Steve's results "
                   "are based on experiment done on a group of students taking "
                   "the same class, which is highly unlikely to generalize to "
                   "the US population."))

    return mc_sol


def solution_mult_choice_lab3():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab3 q1
    mc_sol.append((3, 1, 'a',
                   "The correct answer is B. "
                   "Notice that the experimenters had no control over the bug "
                   "and they are simply measuring the differences in "
                   "productivity level between the two groups (the nature of "
                   "the occurrence resembles random assignment)."))
    mc_sol.append((3, 1, "c",
                   "The correct answer is B. "
                   "Notice that the experimenters had no control over the bug "
                   "and they are simply measuring the differences in "
                   "productivity level between the two groups (the nature of "
                   "the occurrence resembles random assignment)."))
    mc_sol.append((3, 1, "d",
                   "The correct answer is B. "
                   "Notice that the experimenters had no control over the bug "
                   "and they are simply measuring the differences in "
                   "productivity level between the two groups (the nature of "
                   "the occurrence resembles random assignment)."))
    mc_sol.append((3, 1, "e",
                   "The correct answer is B. "
                   "Notice that the experimenters had no control over the bug "
                   "and they are simply measuring the differences in "
                   "productivity level between the two groups (the nature of "
                   "the occurrence resembles random assignment)."))

    # lab3 q2
    mc_sol.append((3, 2, "b",
                   "The correct answer is A. "
                   "The key feature here is random assignment, which makes "
                   "this a true experiment.  The fact that the sample isn’t "
                   "random doesn’t change the type of experiment, it just "
                   "calls into question the external validity of the study. "
                   "A quasi-experiment would imply that there is no random "
                   "assignment.  Finally, it’s clear from the time-structure "
                   "that this is a pretest-posttest design."))
    mc_sol.append((3, 2, "c",
                   "The correct answer is A. "
                   "The key feature here is random assignment, which makes "
                   "this a true experiment.  The fact that the sample isn’t "
                   "random doesn’t change the type of experiment, it just "
                   "calls into question the external validity of the study. "
                   "A quasi-experiment would imply that there is no random "
                   "assignment.  Finally, it’s clear from the time-structure "
                   "that this is a pretest-posttest design."))
    mc_sol.append((3, 2, "d",
                   "The correct answer is A. "
                   "The key feature here is random assignment, which makes "
                   "this a true experiment.  The fact that the sample isn’t "
                   "random doesn’t change the type of experiment, it just "
                   "calls into question the external validity of the study. "
                   "A quasi-experiment would imply that there is no random "
                   "assignment.  Finally, it’s clear from the time-structure "
                   "that this is a pretest-posttest design."))
    mc_sol.append((3, 2, "e",
                   "The correct answer is A. "
                   "The key feature here is random assignment, which makes "
                   "this a true experiment.  The fact that the sample isn’t "
                   "random doesn’t change the type of experiment, it just "
                   "calls into question the external validity of the study. "
                   "A quasi-experiment would imply that there is no random "
                   "assignment.  Finally, it’s clear from the time-structure "
                   "that this is a pretest-posttest design."))

    # lab3 q3
    mc_sol.append((3, 3, "a",
                   "The correct answer is B. "
                   "One of the main motivations for using parametric tests is "
                   "the high power they have.  One way to explain this is "
                   "that they don’t throw away as much information as "
                   "non-parametric tests.  Another way to see this is that "
                   "we’re trying to estimate something about our population, "
                   "say the mean or some other parameter.  In a non-parametric "
                   "test, we begin by assuming almost nothing about the "
                   "population, then we try to narrow down our model using "
                   "the data.  In a parametric test, we begin with a specific "
                   "class of models the population can belong to, then narrow "
                   "these down to an even smaller set using our data, so the "
                   "resulting estimate is more precise.  Hence, we can "
                   "usually expect higher power."))
    mc_sol.append((3, 3, "c",
                   "The correct answer is B. "
                   "One of the main motivations for using parametric tests is "
                   "the high power they have.  One way to explain this is "
                   "that they don’t throw away as much information as "
                   "non-parametric tests.  Another way to see this is that "
                   "we’re trying to estimate something about our population, "
                   "say the mean or some other parameter.  In a non-parametric "
                   "test, we begin by assuming almost nothing about the "
                   "population, then we try to narrow down our model using "
                   "the data.  In a parametric test, we begin with a specific "
                   "class of models the population can belong to, then narrow "
                   "these down to an even smaller set using our data, so the "
                   "resulting estimate is more precise.  Hence, we can "
                   "usually expect higher power."))
    mc_sol.append((3, 3, "d",
                   "The correct answer is B. "
                   "One of the main motivations for using parametric tests is "
                   "the high power they have.  One way to explain this is "
                   "that they don’t throw away as much information as "
                   "non-parametric tests.  Another way to see this is that "
                   "we’re trying to estimate something about our population, "
                   "say the mean or some other parameter.  In a non-parametric "
                   "test, we begin by assuming almost nothing about the "
                   "population, then we try to narrow down our model using "
                   "the data.  In a parametric test, we begin with a specific "
                   "class of models the population can belong to, then narrow "
                   "these down to an even smaller set using our data, so the "
                   "resulting estimate is more precise.  Hence, we can "
                   "usually expect higher power."))
    mc_sol.append((3, 3, "e",
                   "The correct answer is B. "
                   "One of the main motivations for using parametric tests is "
                   "the high power they have.  One way to explain this is "
                   "that they don’t throw away as much information as "
                   "non-parametric tests.  Another way to see this is that "
                   "we’re trying to estimate something about our population, "
                   "say the mean or some other parameter.  In a non-parametric "
                   "test, we begin by assuming almost nothing about the "
                   "population, then we try to narrow down our model using "
                   "the data.  In a parametric test, we begin with a specific "
                   "class of models the population can belong to, then narrow "
                   "these down to an even smaller set using our data, so the "
                   "resulting estimate is more precise.  Hence, we can "
                   "usually expect higher power."))
    mc_sol.append((3, 3, "f",
                   "The correct answer is B. "
                   "One of the main motivations for using parametric tests is "
                   "the high power they have.  One way to explain this is "
                   "that they don’t throw away as much information as "
                   "non-parametric tests.  Another way to see this is that "
                   "we’re trying to estimate something about our population, "
                   "say the mean or some other parameter.  In a non-parametric "
                   "test, we begin by assuming almost nothing about the "
                   "population, then we try to narrow down our model using "
                   "the data.  In a parametric test, we begin with a specific "
                   "class of models the population can belong to, then narrow "
                   "these down to an even smaller set using our data, so the "
                   "resulting estimate is more precise.  Hence, we can "
                   "usually expect higher power."))

    # lab3 q4
    mc_sol.append((3, 4, "a",
                   "The correct answer is C. "
                   "Because the students who are posting puppies and kittens "
                   "are the same population, dependent t-test here would be "
                   "more appropriate (In this case the posting of puppies "
                   "and kittens are like time1 and time2). Because we have "
                   "a large sample size (>30), you can apply the CLT to gain "
                   "normality of sample means, so the dependent t-test is "
                   "appropriate."))
    mc_sol.append((3, 4, "b",
                   "The correct answer is C. "
                   "Because the students who are posting puppies and kittens "
                   "are the same population, dependent t-test here would be "
                   "more appropriate (In this case the posting of puppies "
                   "and kittens are like time1 and time2). Because we have "
                   "a large sample size (>30), you can apply the CLT to gain "
                   "normality of sample means, so the dependent t-test is "
                   "appropriate."))
    mc_sol.append((3, 4, "d",
                   "The correct answer is C. "
                   "Because the students who are posting puppies and kittens "
                   "are the same population, dependent t-test here would be "
                   "more appropriate (In this case the posting of puppies "
                   "and kittens are like time1 and time2). Because we have "
                   "a large sample size (>30), you can apply the CLT to gain "
                   "normality of sample means, so the dependent t-test is "
                   "appropriate."))
    mc_sol.append((3, 4, "e",
                   "The correct answer is C. "
                   "Because the students who are posting puppies and kittens "
                   "are the same population, dependent t-test here would be "
                   "more appropriate (In this case the posting of puppies "
                   "and kittens are like time1 and time2). Because we have "
                   "a large sample size (>30), you can apply the CLT to gain "
                   "normality of sample means, so the dependent t-test is "
                   "appropriate."))
    mc_sol.append((3, 4, "f",
                   "The correct answer is C. "
                   "Because the students who are posting puppies and kittens "
                   "are the same population, dependent t-test here would be "
                   "more appropriate (In this case the posting of puppies "
                   "and kittens are like time1 and time2). Because we have "
                   "a large sample size (>30), you can apply the CLT to gain "
                   "normality of sample means, so the dependent t-test is "
                   "appropriate."))

    # lab3 q5
    mc_sol.append((3, 5, "a",
                   "The correct answer is D. "
                   "We know that P(wear plaid AND drink beer) = P(wear plaid) "
                   "* P(drink beer given wear plaid). However since we have "
                   "the independence assumption, we can simplify "
                   "P(drink beer given wear plaid) = P(drink beer), which "
                   "gives us 42 people when you consider the sample size"))
    mc_sol.append((3, 5, "b",
                   "The correct answer is D. "
                   "We know that P(wear plaid AND drink beer) = P(wear plaid) "
                   "* P(drink beer given wear plaid). However since we have "
                   "the independence assumption, we can simplify "
                   "P(drink beer given wear plaid) = P(drink beer), which "
                   "gives us 42 people when you consider the sample size"))
    mc_sol.append((3, 5, "c",
                   "The correct answer is D. "
                   "We know that P(wear plaid AND drink beer) = P(wear plaid) "
                   "* P(drink beer given wear plaid). However since we have "
                   "the independence assumption, we can simplify "
                   "P(drink beer given wear plaid) = P(drink beer), which "
                   "gives us 42 people when you consider the sample size"))
    mc_sol.append((3, 5, "e",
                   "The correct answer is D. "
                   "We know that P(wear plaid AND drink beer) = P(wear plaid) "
                   "* P(drink beer given wear plaid). However since we have "
                   "the independence assumption, we can simplify "
                   "P(drink beer given wear plaid) = P(drink beer), which "
                   "gives us 42 people when you consider the sample size"))
    mc_sol.append((3, 5, "f",
                   "The correct answer is D. "
                   "We know that P(wear plaid AND drink beer) = P(wear plaid) "
                   "* P(drink beer given wear plaid). However since we have "
                   "the independence assumption, we can simplify "
                   "P(drink beer given wear plaid) = P(drink beer), which "
                   "gives us 42 people when you consider the sample size"))

    # lab3 q6
    mc_sol.append((3, 6, "a",
                   "The correct answer is C. "
                   "Post-hoc adjustments (like Bonferonni) should not be run "
                   "if there is a theoretical reason to suspect that December "
                   "is different than all other months. However, if there is "
                   "no such theoretical basis and the researcher is merely "
                   "exploring the data to see if there are differences "
                   "between the months, then some sort of post-hoc corrections "
                   "should be conducted"))
    mc_sol.append((3, 6, "b",
                   "The correct answer is C. "
                   "Post-hoc adjustments (like Bonferonni) should not be run "
                   "if there is a theoretical reason to suspect that December "
                   "is different than all other months. However, if there is "
                   "no such theoretical basis and the researcher is merely "
                   "exploring the data to see if there are differences "
                   "between the months, then some sort of post-hoc corrections "
                   "should be conducted"))
    mc_sol.append((3, 6, "d",
                   "The correct answer is C. "
                   "Post-hoc adjustments (like Bonferonni) should not be run "
                   "if there is a theoretical reason to suspect that December "
                   "is different than all other months. However, if there is "
                   "no such theoretical basis and the researcher is merely "
                   "exploring the data to see if there are differences "
                   "between the months, then some sort of post-hoc corrections "
                   "should be conducted"))

    # lab3 q7
    mc_sol.append((3, 7, "a",
                   "The correct answer is B. "
                   "Because of the non-random sampling of the population, "
                   "we introduce sampling bias (as opposed to selection "
                   "bias), which puts external validity in question."))
    mc_sol.append((3, 7, "c",
                   "The correct answer is B. "
                   "Because of the non-random sampling of the population, "
                   "we introduce sampling bias (as opposed to selection "
                   "bias), which puts external validity in question."))
    mc_sol.append((3, 7, "d",
                   "The correct answer is B. "
                   "Because of the non-random sampling of the population, "
                   "we introduce sampling bias (as opposed to selection "
                   "bias), which puts external validity in question."))
    mc_sol.append((3, 7, "e",
                   "The correct answer is B. "
                   "Because of the non-random sampling of the population, "
                   "we introduce sampling bias (as opposed to selection "
                   "bias), which puts external validity in question."))
    mc_sol.append((3, 7, "f",
                   "The correct answer is B. "
                   "Because of the non-random sampling of the population, "
                   "we introduce sampling bias (as opposed to selection "
                   "bias), which puts external validity in question."))

    # q8
    mc_sol.append((1, 8, "a",
                   "The correct answer is B. "
                   "Since we're evaluating the effect size, we would like to "
                   "include standard deviation in our consideration, such as "
                   "Cohen's d."))
    mc_sol.append((1, 8, "c",
                   "The correct answer is B. "
                   "Since we're evaluating the effect size, we would like to "
                   "include standard deviation in our consideration, such as "
                   "Cohen's d."))
    mc_sol.append((1, 8, "d",
                   "The correct answer is B. "
                   "Since we're evaluating the effect size, we would like to "
                   "include standard deviation in our consideration, such as "
                   "Cohen's d."))

    return mc_sol


def solution_mult_choice_lab4():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab4 q1
    mc_sol.append((4, 1, 'a', "The correct answer is D. "
                   "As stated in the video lecture, ANOVA is great for "
                   "significance testing, especially in the multivariate case. "
                   "Here we are dealing with the overall model so this is "
                   "not appropriate"))
    mc_sol.append((4, 1, 'b', "The correct answer is D. "
                   "As stated in the video lecture, ANOVA is great for "
                   "significance testing, especially in the multivariate case. "
                   "OLS does not compute statistical significance."))
    mc_sol.append((4, 1, 'c', "The correct answer is D. "
                   "As stated in the video lecture, ANOVA is great for "
                   "significance testing, especially in the multivariate case. "
                   "Notice here that the assumptions are not met"))
    mc_sol.append((4, 1, 'e', "The correct answer is D. "
                   "As stated in the video lecture, ANOVA is great for "
                   "significance testing, especially in the multivariate case. "
                   ""))
    mc_sol.append((4, 1, 'f', "The correct answer is D. "
                   "As stated in the video lecture, ANOVA is great for "
                   "significance testing, especially in the multivariate case. "
                   "Here we are interested in the overall model rather than "
                   "individual variables"))

    # lab4 q2
    mc_sol.append((4, 2, "a", "The correct answer is B. "
                   "As stated in the video lecture, the null is assuming that "
                   "every variable coefficient (so not the b0 term) is zero. "
                   "From what we have learned about forming null hypotheses "
                   "in the class, this makes intuitive sense as it is very "
                   "specific and quantifiable so the criteria for rejecting "
                   "the null is clear."))
    mc_sol.append((4, 2, "c", "The correct answer is B. "
                   "As stated in the video lecture, the null is assuming that "
                   "every variable coefficient (so not the b0 term) is zero. "
                   "From what we have learned about forming null hypotheses "
                   "in the class, this makes intuitive sense as it is very "
                   "specific and quantifiable so the criteria for rejecting "
                   "the null is clear."))
    mc_sol.append((4, 2, "d", "The correct answer is B. "
                   "As stated in the video lecture, the null is assuming that "
                   "every variable coefficient (so not the b0 term) is zero. "
                   "From what we have learned about forming null hypotheses "
                   "in the class, this makes intuitive sense as it is very "
                   "specific and quantifiable so the criteria for rejecting "
                   "the null is clear."))
    mc_sol.append((4, 2, "e", "The correct answer is B. "
                   "As stated in the video lecture, the null is assuming that "
                   "every variable coefficient (so not the b0 term) is zero. "
                   "From what we have learned about forming null hypotheses "
                   "in the class, this makes intuitive sense as it is very "
                   "specific and quantifiable so the criteria for rejecting "
                   "the null is clear."))

    # lab4 q3
    mc_sol.append((4, 3, "a", "The correct answer is E. "
                   "As long as there is a statistically significant "
                   "relationship between one independent variable and the "
                   "dependent variable we can reject the null."))
    mc_sol.append((4, 3, "b", "The correct answer is E. "
                   "b0 is the intercept, it does not really make sense for "
                   "an intercept to be statistically significant"))
    mc_sol.append((4, 3, "c", "The correct answer is E. "
                   "As a counter example, take b2 to be not equal to 0 but "
                   "b1 = 0. We would still reject the null"))
    mc_sol.append((4, 3, "d", "The correct answer is E. "
                   "Requires other information (like the goodness of fit)"))

    # lab4 q4
    mc_sol.append((4, 4, "a", "The correct answer is B. "
                   "everything seems like legitimate indicators of surviving "
                   "in the wild - however the number of pushups in 3 minutes "
                   "should intuitively be highly correlated/collinear with "
                   "the triceps strength (X2)."))
    mc_sol.append((4, 4, "c", "The correct answer is B. "
                   "everything seems like legitimate indicators of surviving "
                   "in the wild - however the number of pushups in 3 minutes "
                   "should intuitively be highly correlated/collinear with "
                   "the triceps strength (X2)."))
    mc_sol.append((4, 4, "d", "The correct answer is B. "
                   "everything seems like legitimate indicators of surviving "
                   "in the wild - however the number of pushups in 3 minutes "
                   "should intuitively be highly correlated/collinear with "
                   "the triceps strength (X2)."))
    mc_sol.append((4, 4, "e", "The correct answer is B. "
                   "everything seems like legitimate indicators of surviving "
                   "in the wild - however the number of pushups in 3 minutes "
                   "should intuitively be highly correlated/collinear with "
                   "the triceps strength (X2)."))

    # lab4 q5
    mc_sol.append((4, 5, "a", "The correct answer is D. "
                   "Notice that here you are controlling the experiment"))
    mc_sol.append((4, 5, "b", "The correct answer is D. "
                   "Notice that here you are manipulating the situation by "
                   "giving questionnaires."))
    mc_sol.append((4, 5, "c", "The correct answer is D. "
                   "Notice that here you are manipulating the situation by"
                   "giving questionnaires"))
    mc_sol.append((4, 5, "e", "The correct answer is D. "
                   "This is not a good design for the research question at "
                   "hand because location will convolute the results"))

    # lab4 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "Well this is kind of obvious you don't need a theorem to "
                   "know this"))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # lab4 q7
    mc_sol.append((1, 7, "7b", "The correct answer is A. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "7c", "The correct answer is A. "
                   "It should actually be larger"))
    mc_sol.append((1, 7, "7d", "The correct answer is A. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "7e", "The correct answer is A. "
                   "That's not what central limit theorem tells us"))
    mc_sol.append((1, 7, "7f", "The correct answer is A. "
                   ""))

    # lab4 q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # lab4 q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult_choice(lab):
    """ generates solutions for multiple choice for specified lab
    """
    if lab == 1:
        mc_sol = solution_mult_choice_lab1()
    elif lab == 2:
        mc_sol = solution_mult_choice_lab2()
    elif lab == 3:
        mc_sol = solution_mult_choice_lab3()
    elif lab == 4:
        mc_sol = solution_mult_choice_lab4()
    else:
        print("Invalid input for lab number (1-4)")
        mc_sol = []
    return mc_sol


def solution_test_selection_lab2():
    """ solution bank for test selection - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        ts_sol (list):          list of tuples to be fed into sqlite database

    """
    ts_sol = []
    # lab2 q1
    ts_sol.append((2, 1, 'a', "The correct answer is B."
                   "Here we want to assess the equality of variances, which is "
                   "exactly what Levenes does."))
    ts_sol.append((2, 1, 'c', "The correct answer is B."
                   "Here we want to assess the equality of variances, which is "
                   "exactly what Levenes does."))

    # lab2 q2
    ts_sol.append((2, 2, "b", "The correct answer is A. "
                   "This is used to determine whether a given set of data "
                   "follows a normal distribution"))
    ts_sol.append((2, 2, "c", "The correct answer is A. "
                   "This is used to determine whether a given set of data "
                   "follows a normal distribution"))

    return ts_sol


def solution_test_selection_lab3():
    """ solution bank for test selection - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        ts_sol (list):          list of tuples to be fed into sqlite database

    """
    ts_sol = []
    # lab3 q1
    ts_sol.append((3, 1, 'a',
                   "The correct answer is D. "
                   "Notice that the income variable is not continuous "
                   "(segmented into ordinal ranges) so we would prefer to use "
                   "a non-parametric test"))
    ts_sol.append((3, 1, 'b',
                   "The correct answer is D. "
                   "Here you’re comparing means between the two categories "
                   "so correlation isn’t gonna be helpful"))
    ts_sol.append((3, 1, 'c',
                   "The correct answer is D. "
                   "Recall that signed rank test is for when the data are "
                   "paired - which is not the case here, so the rank-sum "
                   "is a better choice"))
    ts_sol.append((3, 1, 'e',
                   "The correct answer is D. "
                   "A chi-square could be used since income isn’t an interval "
                   "variable, but it throws away a lot more information than "
                   "the rank sum test.  The rank sum test also gets at the "
                   "question of which group has higher income, and this is "
                   "harder to interpret from a significant chi-square result."))
    ts_sol.append((3, 1, 'f',
                   "The correct answer is D. "
                   "Here we have only two groups, rank-sum would be a better "
                   "approach."))

    # lab3 q2
    ts_sol.append((3, 2, "a",
                   "The correct answer is D. "
                   "Notice that the country music is a categorical variable "
                   "with 7 different categories thus it’s best to use ANOVA"))
    ts_sol.append((3, 2, "b",
                   "The correct answer is D. "
                   "Notice that the country music is a categorical variable "
                   "with 7 different categories thus it’s best to use ANOVA"))
    ts_sol.append((3, 2, "c",
                   "The correct answer is D. "
                   "Notice that the country music is a categorical variable "
                   "with 7 different categories thus it’s best to use ANOVA"))
    ts_sol.append((3, 2, "e",
                   "The correct answer is D. "
                   "Notice that the country music is a categorical variable "
                   "with 7 different categories thus it’s best to use ANOVA"))

    # lab3 q3
    ts_sol.append((3, 3, "b",
                   "The correct answer is A. "
                   "After cleaning the data to arrive at the observations "
                   "with the conditions sex=='Male' and relig=='Catholic' "
                   "(and the female counterpart), "
                   "we see that there are 130/203 for male/female catholics. "
                   "This sample size is large enough (>30) to use the t-test "
                   "thanks to CLT. Also notice that the t-test assumes the "
                   "means of the samples are normally distributed; it does "
                   "not assume that the population (the hist() we see) is "
                   "normally distributed."))
    ts_sol.append((3, 3, "c",
                   "The correct answer is A. "
                   "After cleaning the data to arrive at the observations "
                   "with the conditions sex=='Male' and relig=='Catholic' "
                   "(and the female counterpart), "
                   "we see that there are 130/203 for male/female catholics. "
                   "This sample size is large enough (>30) to use the t-test "
                   "thanks to CLT. Also notice that the t-test assumes the "
                   "means of the samples are normally distributed; it does "
                   "not assume that the population (the hist() we see) is "
                   "normally distributed."))
    ts_sol.append((3, 3, "d",
                   "The correct answer is A. "
                   "After cleaning the data to arrive at the observations "
                   "with the conditions sex=='Male' and relig=='Catholic' "
                   "(and the female counterpart), "
                   "we see that there are 130/203 for male/female catholics. "
                   "This sample size is large enough (>30) to use the t-test "
                   "thanks to CLT. Also notice that the t-test assumes the "
                   "means of the samples are normally distributed; it does "
                   "not assume that the population (the hist() we see) is "
                   "normally distributed."))
    ts_sol.append((3, 3, "e",
                   "The correct answer is A. "
                   "After cleaning the data to arrive at the observations "
                   "with the conditions sex=='Male' and relig=='Catholic' "
                   "(and the female counterpart), "
                   "we see that there are 130/203 for male/female catholics. "
                   "This sample size is large enough (>30) to use the t-test "
                   "thanks to CLT. Also notice that the t-test assumes the "
                   "means of the samples are normally distributed; it does "
                   "not assume that the population (the hist() we see) is "
                   "normally distributed."))
    ts_sol.append((3, 3, "f",
                   "The correct answer is A. "
                   "After cleaning the data to arrive at the observations "
                   "with the conditions sex=='Male' and relig=='Catholic' "
                   "(and the female counterpart), "
                   "we see that there are 130/203 for male/female catholics. "
                   "This sample size is large enough (>30) to use the t-test "
                   "thanks to CLT. Also notice that the t-test assumes the "
                   "means of the samples are normally distributed; it does "
                   "not assume that the population (the hist() we see) is "
                   "normally distributed."))

    # lab3 q4
    ts_sol.append((3, 4, "a",
                   "The correct answer is B. "
                   "Since both variables are continuous, Pearson correlation "
                   "is the best option."))
    ts_sol.append((3, 4, "c",
                   "The correct answer is B. "
                   "Since both variables are continuous, Pearson correlation "
                   "is the best option."))
    ts_sol.append((3, 4, "d",
                   "The correct answer is B. "
                   "Since both variables are continuous, Pearson correlation "
                   "is the best option."))
    ts_sol.append((3, 4, "e",
                   "The correct answer is B. "
                   "Since both variables are continuous, Pearson correlation "
                   "is the best option."))
    ts_sol.append((3, 4, "f",
                   "The correct answer is B. "
                   "Since both variables are continuous, Pearson correlation "
                   "is the best option."))

    # lab3 q5
    ts_sol.append((3, 5, "a",
                   "The correct answer is D. "
                   "Notice here we have two categorical variables and the "
                   "requirements to use a Chi-Square are met so we should "
                   "use it."))
    ts_sol.append((3, 5, "b",
                   "The correct answer is D. "
                   "Notice here we have two categorical variables and the "
                   "requirements to use a Chi-Square are met so we should "
                   "use it."))
    ts_sol.append((3, 5, "c",
                   "The correct answer is D. "
                   "Notice here we have two categorical variables and the "
                   "requirements to use a Chi-Square are met so we should "
                   "use it."))
    ts_sol.append((3, 5, "e",
                   "The correct answer is D. "
                   "Notice here we have two categorical variables and the "
                   "requirements to use a Chi-Square are met so we should "
                   "use it."))

    return ts_sol


def solution_test_selection_lab4():
    """ solution bank for test selection - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        ts_sol (list):          list of tuples to be fed into sqlite database

    """
    ts_sol = []
    # lab4 q1
    ts_sol.append((4, 1, 'b', "The correct answer is A."
                   "Since it is categorical data we are dealing with here, "
                   "chi-square is the best way to go."))
    ts_sol.append((4, 1, 'c', "The correct answer is A."
                   "Since it is categorical data we are dealing with here, "
                   "chi-square is the best way to go."))
    ts_sol.append((4, 1, 'd', "The correct answer is A."
                   "Since it is categorical data we are dealing with here, "
                   "chi-square is the best way to go."))

    # lab4 q2
    ts_sol.append((4, 2, "a", "The correct answer is D. "
                   "Note that region has more than two categories, so all the "
                   "other tests do not really work."))
    ts_sol.append((4, 2, "b", "The correct answer is D. "
                   "Note that region has more than two categories, so all the "
                   "other tests do not really work."))
    ts_sol.append((4, 2, "c", "The correct answer is D. "
                   "Note that region has more than two categories, so all the "
                   "other tests do not really work."))

    # lab4 q3
    ts_sol.append((4, 3, "a", "The correct answer is B. "
                   "Notice that the sample size is big enough that we can "
                   "invoke CLT for normality assumptions. Choice A is too "
                   "restricting."))
    ts_sol.append((4, 3, "c", "The correct answer is B. "
                   "Notice that the sample size is big enough that we can "
                   "invoke CLT for normality assumptions. We do not really "
                   "have dependent samples for choice C"))
    ts_sol.append((4, 3, "d", "The correct answer is B. "
                   "Notice that the sample size is big enough that we can "
                   "invoke CLT for normality assumptions. Choice D does not "
                   "make much sense as there is only one independent "
                   "variable."))

    # lab4 q4
    ts_sol.append((4, 4, "a", "The correct answer is B. "
                   "Here we are dealing with more than two categories so "
                   "certainly not choice C nor D. ANOVA is preferred over "
                   "chi-square because the adults in household variable "
                   "is ordinal."))
    ts_sol.append((4, 4, "c", "The correct answer is B. "
                   "Here we are dealing with more than two categories so "
                   "certainly not choice C nor D. ANOVA is preferred over "
                   "chi-square because the adults in household variable "
                   "is ordinal."))
    ts_sol.append((4, 4, "d", "The correct answer is B. "
                   "Here we are dealing with more than two categories so "
                   "certainly not choice C nor D. ANOVA is preferred over "
                   "chi-square because the adults in household variable "
                   "is ordinal."))

    # lab4 q5
    ts_sol.append((4, 5, "b", "The correct answer is A. "
                   "Notice that both variables are metric and the sample size "
                   "is big enough for meeting normality assumptions that "
                   "Pearson correlation is best for measuring their "
                   "relationship."))
    ts_sol.append((4, 5, "c", "The correct answer is A. "
                   "Notice that both variables are metric and the sample size "
                   "is big enough for meeting normality assumptions that "
                   "Pearson correlation is best for measuring their "
                   "relationship."))
    ts_sol.append((4, 5, "d", "The correct answer is A. "
                   "Notice that both variables are metric and the sample size "
                   "is big enough for meeting normality assumptions that "
                   "Pearson correlation is best for measuring their "
                   "relationship."))

    # lab4 q6
    ts_sol.append((4, 6, "a", "The correct answer is B. "
                   "Because of the rather small size, we cannot rely on CLT "
                   "for the normality assumptions. Thus a non-parametric test "
                   "like Wilcoxon Rank-Sum Test is best here to compare a "
                   "rankable metric variable in two independent groups."))
    ts_sol.append((4, 6, "a", "The correct answer is B. "
                   "Because of the rather small size, we cannot rely on CLT "
                   "for the normality assumptions. Thus a non-parametric test "
                   "like Wilcoxon Rank-Sum Test is best here to compare a "
                   "rankable metric variable in two independent groups."))
    ts_sol.append((4, 6, "a", "The correct answer is B. "
                   "Because of the rather small size, we cannot rely on CLT "
                   "for the normality assumptions. Thus a non-parametric test "
                   "like Wilcoxon Rank-Sum Test is best here to compare a "
                   "rankable metric variable in two independent groups."))

    return ts_sol


def solution_test_selection(lab):
    """ generates solutions for test selection for specified lab
    """
    if lab == 2:
        ts_sol = solution_test_selection_lab2()
    elif lab == 3:
        ts_sol = solution_test_selection_lab3()
    elif lab == 4:
        ts_sol = solution_test_selection_lab4()
    else:
        print("Invalid input for lab number (1-4)")
        ts_sol = []
    return ts_sol


def write_mc_to_db(lab):
    """ writes mc_sol to database "solutions.db"
    Args:
        lab:            lab number for which the solution is to be written
    """
    con = lite.connect('solutions.db')
    mc_sol = solution_mult_choice(lab)

    with con:
        cur = con.cursor()
        for i in range(len(mc_sol)):
            cur.execute("INSERT INTO MC VALUES{0}".format(mc_sol[i]))


def write_ts_to_db(lab):
    """ writes ts_sol to database "solutions.db"
    Args:
        lab:            lab number for which the solution is to be written
    """
    con = lite.connect('solutions.db')
    ts_sol = solution_test_selection(lab)

    with con:
        cur = con.cursor()
        for i in range(len(ts_sol)):
            cur.execute("INSERT INTO TS VALUES{0}".format(ts_sol[i]))

if __name__ == "__main__":
    write_mc_to_db(3)
    write_ts_to_db(3)
