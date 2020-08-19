import calculate_AE as cAE
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("--file_path", required=True, help="operand file_path")
ap.add_argument("--plot", required=False, help="Plot graph True./False", default=False)
ap.add_argument("--plotFileName", required=False, help="file name of plotted graph")
ap.add_argument("--testAuto", required=False, help="run auto test or not", default=False)
ap.add_argument("--AutoTestPath", required=False, help="path to json files tested")
args = vars((ap.parse_args()))
if args['plot'] == True and args['plotFileName'] == None:
    ap.error("plotting requires file name destination")
if args['testAuto'] == True and args['AutoTestPath'] == False:
    ap.error("Auto test requires a path")

def CheckResult(actualRes, ExpectedRes):
    print("ExpectedRes = {}".format(ExpectedRes))
    print("actualRes = {}".format(actualRes))
    print(actualRes == ExpectedRes)

def main():
    p1 = cAE.AccumAE()
    if (args['testAuto'] == False):
        print("Propagated statistics = {}".format(p1.CalcPropStats(args['file_path'],
                                                                   args['plot'],
                                                                   args['plotFileName'])))
    else:
        expectedRes = [15.8, 66.9, 1.3, 40.2]
        listOfFileNames = os.listdir(args['AutoTestPath'])
        listOfFileNames.sort()
        expectedResIndex = 0;
        for fileName in listOfFileNames:
            if fileName.endswith(".json"):
                CheckResult(p1.CalcPropStats(args['AutoTestPath'] + fileName,
                                             args['plot'],
                                             os.path.splitext(fileName)[0]),
                            expectedRes[expectedResIndex])
                expectedResIndex += 1


if __name__ == "__main__":
    main()