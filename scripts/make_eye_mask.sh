# if identifier starts with number
for i in 0 1 2 3 4 5 6 7 8 9 ; do 
python scripts/Main.py "${1}*_t1w.nii.gz" &
done
# if identifer starts with character
for j in {a..z} ; do
python scripts/Main.py "${j}*_t1w.nii.gz" &
done 
# My first bash script (swag)
