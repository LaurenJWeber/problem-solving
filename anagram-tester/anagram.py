import argparse
name = "anagram"


class AnagramTester:

    def anagram_test(self, string1: str, string2: str) -> bool:
        string1 = self._remove_non_alphanumerics(string1.lower())
        string2 = self._remove_non_alphanumerics(string2.lower())
        string1_dict = {}
        string2_dict = {}

        for char in string1:
            if char not in string1_dict.keys():
                string1_dict[char] = 1
            else:
                string1_dict[char] += 1

        for char in string2:
            if char not in string2_dict.keys():
                string2_dict[char] = 1
            else:
                string2_dict[char] += 1

        return string1_dict == string2_dict

    def _remove_non_alphanumerics(self, input_string: str) -> str:
        output_string = ""
        for char in input_string:
            if char.isalnum():
                output_string += char
        return output_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string1", type=str, help="First string")
    parser.add_argument("string2", type=str, help="Second string")
    args = parser.parse_args()
    anagram_tester = AnagramTester()
    result = anagram_tester.anagram_test(args.string1, args.string2)

    print(f"Inputs were: \n{args.string1}\n{args.string2}")
    if result:
        print("They are anagrams.")
    else:
        print("They are not anagrams.")


if __name__ == "__main__":
    main()
