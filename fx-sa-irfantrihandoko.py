import random
import math

# parameter untuk Simulated Annealing (T = Temperatur)
TMax = 1000
TMin = 0
TCooler = 0.5

# fungsi x1 dan x2 
def fxc(x1, x2):
    return (4 - 2.1 * x1**2 + x1**4/3)*x1**2 + x1 * x2 + (-4 + 4 * x2**2) * x2**2

# metode simuulated annealing dengan parameter untuk eksperimen(temperatur maksimal, minimum, dan pendingin)
def SA(TMax, TMin, TCooler):

	# random angka dari range -10 sampai 10 untuk mendapatkan x1 dan x2
	x1 = random.uniform(-10.0, 10.0)
	x2 = random.uniform(-10.0, 10.0)

	# current state untuk memperoleh state pertama kalinya yang digunakan untuk mengeksekusi f(x1, x2)
	currentState = []
	currentState.append(x1)
	currentState.append(x2)
	fx = fxc(x1, x2)

	# variabel untuk mengolah output program (best so far/nilai minimum fungsi dan iterasinya)
	bestSoFar = 0
	iterations = 0
	bestSoFar = fxc(x1, x2)
	length = []

	# konstan yang digunakan untuk pencarian nilai minimum
	k = 88
	maks = 0

	while TMax > TMin:
		# perhitungan jumlah iterasi temperature sampai minimum
		length.append(1)
		# perulangan pencarian x1 dan x2 secara random sampai menghasilkan nilai minimum
		for i in range(0, k):
			# x1 dan x2 baru secara random
			x1New = random.uniform(-10.0, 10.0)
			x2New = random.uniform(-10.0, 10.0)
			# perolehan new state x1 dan x2
			newState = []
			newState.append(x1New)
			newState.append(x2New)
			# perolehan f(x1, x2) baru
			fxNew = fxc(newState[0], newState[1])
			# perubahan yang dialami nilai f(x1, x2)
			deltaE = fxNew - fx
			if deltaE < 0 :
				# jika kondisi terpenuhi maka memperoleh best so far
				if fxNew < bestSoFar:
					currentState = newState
					bestSoFar = fxNew
					# perolehan jumlah iterasi untuk mendapatkan best so far
					iterations = iterations + 1
			else:
				# probabilitas yang terjadi
				p = math.exp(-deltaE/TMax)
				xRandom = random.uniform(0.0, 1.0)
				if xRandom < p:
					currentState = newState
			# pengecekan untuk memperoleh nilai minimum terbaik dan jika belum memenuhi maka melakukan perulangan random x1 dan x2
			if i == k-1 and bestSoFar > maks:
				k += 1
		# proses penurunan temperatur maksimal menuju minimum
		TMax = TMax * TCooler
	# output 
	print "State: x1: %s, x2: %s" % (currentState[0], currentState[1])
	print "Iterations: %s" % (len(length) * iterations)
	print "Best So Far: %s" % (bestSoFar)

def main():
	# pemanggilan metode Simulated Annealing
	SA(TMax, TMin, TCooler)

main()