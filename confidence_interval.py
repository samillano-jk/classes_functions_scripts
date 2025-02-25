import math as m

# Functions
##--
def ci_proportion_z(sample, proportion, z_score):
        percent_p = proportion/sample
        se = m.sqrt((.6*(1-.6))/200)
        me = round(z_score * se, 4)
        lower = round(percent_p - me, 4)
        upper = round(percent_p + me, 4)
        return upper, lower


def ci_mean_z(sample, std, mean, z_score):
        se = std/m.sqrt(sample)
        me = round(z_score * se, 4)
        lower = mean - me
        upper = mean + me
        return upper, lower


def main():
        pick = input("Enter (m)ean/(p)roportion: ").lower()
        if pick == "m":
                sample = int(input("Sample size: "))
                std = int(input("Population std: "))
                mean = int(input("Sample mean: "))
                z_score = float(input("Z score value: "))
                upper, lower = ci_mean_z(sample, std, mean, z_score)
                print(f"CI: {lower} - {upper}")


        elif pick == "p":
                sample = int(input("Sample size: "))
                proportion = int(input("Proportion size: "))
                z_score = float(input("Z score value: "))
                upper, lower = ci_proportion_z(sample, proportion, z_score)
                print(f"CI: {lower} - {upper}")

        else: 
                print("Invalid")

##--



if __name__ == "__main__":
        main()