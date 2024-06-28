import utils
import sys

def main():
    command = sys.argv[1]
    if command == "m4m":
        make = input("Enter the make for which you want the models of : ").lower().replace(" ", "%20")
        year = input("Enter the year (optional) : ")
        vtype = input("Enter the vehicle's type (optional) : ")
        data = utils.models_for_make(make, year, vtype)
        print("Model_ID\tModel_Name")
        for model in data:
            print(model["Model_ID"],model["Model_Name"],sep="\t\t")

if __name__ == "__main__":
    main()
