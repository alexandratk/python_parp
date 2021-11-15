package ua.nure.tkachenko.task1;

import java.io.PrintWriter;
import java.util.Random;

public class Part4 {

	public static int max;
	public static int[][] matrix;

	public static void main(String []  args) {
		Random random = new Random();
		int n = 10000;
		int m = 10000;
		matrix = new int[n][m];
        for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				matrix[i][j] = random.nextInt(1000 - 1) + 1;
			}
		}
        Part4 obj = new Part4();
        long start = System.currentTimeMillis();
		max = -1000;
		MyThreadPart4[] threads = new MyThreadPart4[matrix.length];
		for (int i = 0; i < matrix.length; i++) {
			threads[i] = new MyThreadPart4(obj, i);
		}
		for (MyThreadPart4 t: threads) {
			t.start();
		}
		
		for (MyThreadPart4 t: threads) {
			try {
				t.join();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		long end = System.currentTimeMillis();
		System.out.println("Max: " + max);
		System.out.println("Time: " + (end - start));
        
        start = System.currentTimeMillis();
		max = -1000;
		for (int i = 0; i < matrix.length; i++) {
        	for (int j = 0; j < matrix[i].length; j++) {
//        		try {
//					Thread.sleep(1);
//				} catch (InterruptedException e) {
//					e.printStackTrace();
//				}
        		if (matrix[i][j] > max) {
        			max = matrix[i][j];
        		}
        	}
        }
		end = System.currentTimeMillis();
		System.out.println("Max: " + max);
		System.out.println("Time: " + (end - start));
	}
	
	public int maxStr(int k) {
		int maxstr = -1000;
		for (int i = 0; i < matrix[k].length; i++) {
//			try {
//				Thread.sleep(1);
//			} catch (InterruptedException e) {
//				e.printStackTrace();
//			}
			if (maxstr < matrix[k][i]) {
				maxstr = matrix[k][i];
			}
		}
		return maxstr;
	}
	
	synchronized public void changeMax(int newMax) {
		if (max < newMax) {
			max = newMax;
		}
	}
	
}

class MyThreadPart4 extends Thread {
	Part4 obj; 
	int k;
	public MyThreadPart4(Part4 obj, int k) {
		this.obj = obj;
		this.k = k;
	}
	
	public void run() {
		int max = obj.maxStr(k);
		obj.changeMax(max);
	}
}
