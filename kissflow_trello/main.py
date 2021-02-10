# This is a sample Python script.

from behave import __main__ as runner_with_options

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    featureFilePath = 'features/feature_files/kissflow.feature'


    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '


    fullRunnerOptions =  featureFilePath  + commonRunnerOptions

    runner_with_options.main(fullRunnerOptions)

