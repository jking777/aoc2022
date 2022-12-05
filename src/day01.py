from data.day01_data import sample_lines, input_lines

sample = False
if sample:
    data = sample_lines
else:
    data = input_lines


def main():
    elf_totals = {}
    elf_num = 1
    elf_max_num = 0
    elf_max = -1
    for line in data:
        if len(line) == 0:
            elf_num += 1
        else:
            elf_total = elf_totals.setdefault(elf_num, 0)
            elf_total += int(line)
            elf_totals[elf_num] = elf_total

            if elf_total > elf_max:
                elf_max = elf_total
                elf_max_num = elf_num

    print(f"Elf # {elf_max_num} has {elf_max} calories")

    # part 2

    sorted_elves_by_total = sorted(elf_totals.items(), key=lambda x: x[1])
    print()
    print(f"Top 3 elves:")
    top3_total = 0
    for i in [-1, -2, -3]:
        elf_info = sorted_elves_by_total[i]
        print(f"Elf {elf_info[0]} has {elf_info[1]} calories")
        top3_total += elf_info[1]
    print(f"Top 3 total calories:  {top3_total}")


if __name__ == "__main__":
    main()
