import utils
import sys

def main():
    command = sys.argv[1].lower()
    if command == "m4m":
        data = utils.models_for_make(sys.argv[2])
        print("Model_ID\tModel_Name")
        for model in data:
            print(model["Model_ID"],model["Model_Name"],sep="\t\t")
    elif command == "vv":
        data = utils.vehicle_variables()
        for row in data:
            print(row["ID"], row["Name"])
            print(row["Description"][3:-4])
            print()
    elif command == "vvv":
        data = utils.vehicle_variable_values(sys.argv[2])
        for row in data:
            print(row)

if __name__ == "__main__":
    main()
