test_dir="/home/dengineer/Desktop/Study/test_automation/Day1/test/"
files=(*)
ext=()

if [ -d "$test_dir" ]; then
        echo "Path exist"
else
        echo "Path not exist"
        exit
fi

for file in "${files[@]}"; do
        ext="${file##*.}"
        if [ -d "$test_dir/$ext" ]; then
                echo "path exist already"
        else
                mkdir $test_dir/$ext
        fi

	if [ -e "$file" ]; then
                mv "$file" $test_dir/$ext
        else
                echo "file not exist"
        fi
done
