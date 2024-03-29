# Feature Importance

Three approaches to determining which features are the "most important" to
the model.

NOTE: transform your features first to make this easier

## 1. Permutation-based feature impact

Repeat the procedure below 1-4 times for each feature.

1. take a sample of 100k rows
2. shuffle one column of training data
3. predict
4. compute the average drop in accuracy
5. normalize the results (most important feature is 100%)

### Randomize in Pandas
df["col4"] = np.random.permutations(df[4].values)

## 2. SHAP (Shapeley Additive exPlanations)

Is a game theoretic approach to explaining output from any machine learning
model.  It connects optimal credit allocations with local explanations
using the classic Shapley values from game theory and their related
extensions:
[https://papers.nips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf](https://papers.nips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf)

1. take a sample of 100k rows
2. compute SHAP values for each record, generating the local importance of
   each feature in each record
3. compute global importance by taking the average ABS(SHAP values) for each
   feature in the sample
4. normalize the results (i.e., the top feature had an impact of 100%)

## 3. Tree-based variable importance

Uses node impurity measures (gini, entropy) to show how much gain each feature
adds to the model.

[https://docs.datarobot.com/en/docs/modeling/analyze-models/other/analyze-insights.html#tree-based-variable-importance](https://docs.datarobot.com/en/docs/modeling/analyze-models/other/analyze-insights.html#tree-based-variable-importance)
