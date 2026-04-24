def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    file_name = input("Enter the tsv file name: ")
    
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            return

        student_data = []
        m1_total = 0
        m2_total = 0
        f_total = 0
        count = 0

        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue
            
            last_name = parts[0]
            first_name = parts[1]
            m1 = int(parts[2])
            m2 = int(parts[3])
            final = int(parts[4])
            
            # 计算个人平均分和等级
            avg = (m1 + m2 + final) / 3
            grade = get_letter_grade(avg)
            
            student_data.append(f"{last_name}\t{first_name}\t{m1}\t{m2}\t{final}\t{grade}")
            
            # 累加用于计算考试平均分
            m1_total += m1
            m2_total += m2
            f_total += final
            count += 1

        # 计算各科平均分
        avg_m1 = m1_total / count
        avg_m2 = m2_total / count
        avg_f = f_total / count

        # 写入 report.txt
        with open('report.txt', 'w') as out_file:
            for row in student_data:
                out_file.write(row + '\n')
            out_file.write(f"\nAverages: midterm1 {avg_m1:.2f}, midterm2 {avg_m2:.2f}, final {avg_f:.2f}\n")
            
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
