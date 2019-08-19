#!/bin/bash
#

insertsort()
{
	for j in `seq 2 $[${#arr[@]}-1]`
	do
		key=${arr[j]}
		i=$[j-1]
		while [ ${arr[i]} -gt $key -a $i -ge 0 ]
		do
			arr[i+1]=${arr[i]}
			let i--
		done
		arr[i+1]=$key
	done
}

mergesort()
{

	if [ $1 -lt $2 ]
	then
		local mid=$[($1+$2)>>1]
		mergesort $1 $[mid]
		mergesort $[mid+1] $2
		declare -a local tmp
		declare -i local i=$1 j=$[mid+1] k=0	
		while [ $i -le $mid -a $j -le $2 ]
		do
			if [ ${arr[i]} -lt ${arr[j]} ]
			then
				tmp[$[k++]]=${arr[$[i++]]}
			else
				tmp[$[k++]]=${arr[$[j++]]}
			fi
		done
		while [ $i -le $mid ]
		do
			tmp[$[k++]]=${arr[$[i++]]}
		done
		while [ $j -le $2 ]
		do
			tmp[$[k++]]=${arr[$[j++]]}
		done
		for ((i=0;i<k;i++))
		{
			arr[$1+i]=${tmp[i]}
		}
	fi
}

quicksort()
{
	if [ $1 -lt $2 ]
	then
		declare -i local i=$1 j=$2
		declare -i local k=${arr[i]}
		while [ $i -lt $j ]
		do
			while [ ${arr[j]} -gt $k ]
			do
				let j--
			done
			arr[$[i++]]=${arr[j]}
			while [ $i -lt $j -a ${arr[i]} -lt $k ]
			do
				let i++
			done
			arr[$[j--]]=${arr[i]}
		done
		arr[i]=$k
		quicksort $1 $[i-1]
		quicksort $[j+1] $2
	fi
}

heapsort1()
{
	local t=$[$1<<1]
	if [ $[t<<1] -le $length ]
	then
		heapsort1 $[t+1]
		heapsort1 $t
	fi


	if [ $t -le $length ]
	then
		i=0
		num=${arr[$1]}
		if [ $num -lt ${arr[$t]} ]
		then
			i=$t
			num=${arr[$t]}
		fi
	
		if [ $t -lt $length ] && [ $num -lt ${arr[$[t+1]]} ]
		then
			i=$[t+1]
			num=${arr[$[t+1]]}
		fi
		if [ $i -ne 0 ]
		then
			arr[$i]=${arr[$1]}
			arr[$1]=$num
		fi
	fi

	if [ $[t<<1] -le $length ]
	then
		heapsort1 $[t+1]
		heapsort1 $t
	fi
}

heapsort2()
{
	i=$[length>>1]
	while [ $i -ge 1 ]
	do
		j=$i
		while [ $[j<<1] -le $length ]
		do
			k=$j
			num=${arr[$j]}
			t=$[j<<1]
			if [ $num -lt ${arr[$t]} ]
			then
				j=$t
				num=${arr[$t]}
			fi
		
			if [ $t -lt $length ] && [ $num -lt ${arr[$[t+1]]} ]
			then
				j=$[t+1]
				num=${arr[$[t+1]]}
			fi
			if [ $j -ne  $k ]
			then
				arr[$j]=${arr[$k]}
				arr[$k]=$num
			else
				break
			fi
		done
		let i--
	done
}

heapsort()
{
	left=1
	right=$length
	while [ $left -lt $right ]
	do
		t=${arr[$left]}
		arr[$[left]]=${arr[$right]}
		arr[$[right--]]=$t

		j=$left
		while [ $[j<<1] -le $right ]
		do
			k=$j
			num=${arr[$j]}
			t=$[j<<1]
			if [ $num -lt ${arr[$t]} ]
			then
				j=$t
				num=${arr[$t]}
			fi
		
			if [ $t -lt $right ] && [ $num -lt ${arr[$[t+1]]} ]
			then
				j=$[t+1]
				num=${arr[$[t+1]]}
			fi
			if [ $j -ne  $k ]
			then
				arr[$j]=${arr[$k]}
				arr[$k]=$num
			else
				break
			fi
		done
	done
	

}


#declare -i starttime=`date +%s%N`
insertsort
echo ${arr[@]}
#declare -i endtime=`date +%s%N`
#echo $[(endtime-starttime)/100000]
#
#for ((i=0;i<3000;i++))
#{
#	arr[$i]=$RANDOM
#}
#declare -i starttime=`date +%s%N`
#mergesort 0 $[${#arr[@]}-1]
#declare -i endtime=`date +%s%N`
#echo $[(endtime-starttime)/100000]
