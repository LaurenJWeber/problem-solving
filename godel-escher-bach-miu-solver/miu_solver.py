import argparse

'''
Brute-force solver for the M-I-U puzzle in Hofstadter's Godel, Escher, Bach, Chapter 1.
Given an initial theorem, e.g. 'mi', apply the four rules to try deriving 'mu'.

We begin with a dictionary containing the initial theorem.
We apply each rule once (if possible) per iteration.  
Any strings derived from applying the rules are added to the dictionary and processed in the next iteration.
'''
class miu_solver:

    def __init__(self, initial_theorem, iterations):
        self.theorems = {initial_theorem: False }
        self.iterations = iterations

    def rule_one(self, theorem):
        '''
        First rule: we can add a 'u' to any string ending in 'i'.
        '''
        if theorem.endswith("i"):
            theorem += "u"
            return theorem
        else:
            return None

    def rule_two(self, theorem):
        '''
        Second rule: we can double any string after M, i.e. Mx => Mxx
        '''
        if theorem.startswith("m") and len(theorem) > 1:
            theorem += theorem[1:]
            return theorem
        else:
            return None

    def rule_three(self, theorem):
        '''
        Third rule: we can replace three consecutive 'i's with a 'u'.
        '''
        position = theorem.find("iii")
        if position < 0:
            return None
        else:            
            theorem_with_replacements = theorem[0:position] + "u" + theorem[position+3:]
            return theorem_with_replacements

    def rule_four(self, theorem):
        '''
        Fourth rule: two consecutive 'u's can be dropped.
        '''
        position = theorem.find("uu")
        if position < 0:
            return None
        else:
            theorem_with_replacements = theorem[0:position] + theorem[position+2:]
            return theorem_with_replacements
        

    def process_rules(self):
        for i in range(1, self.iterations + 1):
            success = False

            results_rule_one = []
            results_rule_two = []
            results_rule_three = []
            results_rule_four = []

            print(f"============= Iteration {i} =============")
            for theorem_under_test in self.theorems.keys():
                if not self.theorems[theorem_under_test]:
                    result_one = self.rule_one(theorem_under_test)
                    result_two = self.rule_two(theorem_under_test)
                    result_three = self.rule_three(theorem_under_test)
                    result_four = self.rule_four(theorem_under_test)

                if result_one is not None:
                    results_rule_one.append(result_one)

                if result_two is not None:
                    results_rule_two.append(result_two)

                if result_three is not None:
                    results_rule_three.append(result_three)

                if result_four is not None:
                    results_rule_four.append(result_four)
                
                self.theorems[theorem_under_test] = True

            for result in results_rule_one:
                if result not in self.theorems.keys():
                    self.theorems[result] = False

            for result in results_rule_two:
                if result not in self.theorems.keys():
                    self.theorems[result] = False

            for result in results_rule_three:
                if result not in self.theorems.keys():
                    self.theorems[result] = False
            
            for result in results_rule_four:
                if result not in self.theorems.keys():
                    self.theorems[result] = False

            for key in self.theorems.keys():
                # print(key)
                if key == "mu":
                    print("*** Found mu! ***")
                    success = True
                    break
            
            print(f"Checked {len(self.theorems.keys())} theorems.")

            if success:
                break
'''
Supply two arguments:
1) The initial theorem, e.g. 'mi'
2) The number of iterations over which to apply the rules.
'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("initial_theorem", type=str)
    parser.add_argument("iterations", type=int)
    args = parser.parse_args()
    my_miu_solver = miu_solver(args.initial_theorem, args.iterations)
    my_miu_solver.process_rules()


if __name__ == "__main__":
    main()
