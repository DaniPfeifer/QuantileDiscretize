def quantileDiscretize(df, numOfIntervals,printPartitions=False):
    cols = list(df.columns)
    colList = [list(df[c]) for c in cols]
    elementsPerCol = [len(set(df[c])) for c in cols]
    if printPartitions:
        i = 0

    def discrCol(L,colname,printPartitions=False):
        Q = np.quantile(L, np.linspace(0, 1, numOfIntervals + 1)[1:-1])
        if printPartitions:
            print("Column", colname, ":", Q)
        intervals = [[l for l in L if l < Q[0]]] + [[l for l in L if Q[i] <= l < Q[i + 1]] for i in
                                                    range(0, numOfIntervals - 2)] + [[l for l in L if Q[-1] <= l]]
        intervalAverages = [np.mean(I) for I in intervals]
        correctIntervals = [min([q if l < Q[q] else len(Q) for q in range(len(Q))]) for l in L]
        return [intervalAverages[cI] for cI in correctIntervals]

    newCols = [discrCol(colList[c],cols[c],printPartitions) if elementsPerCol[c] > numOfIntervals else colList[c] for c in range(len(colList))]
    newdata = dict(zip(cols, newCols))
    return pd.DataFrame(data=newdata)
