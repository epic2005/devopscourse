for ((i=0;i<10;i++))
do 
    printf "get mem test \n" | nc 127.0.0.1 11211
done
