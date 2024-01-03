import static java.lang.Math.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Stack;

public class Main2696 {
	public static void main(String[] args) throws IOException {

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String s = reader.readLine();
		int T = Integer.parseInt(s);
		for (int tmp = 0; tmp < T; tmp++) {

			int size = 0;
			String s1 = reader.readLine();

			int num = Integer.parseInt(s1);

			List<String> stringList = new ArrayList<>();
			for (int i = 0; i < num; i += 10) {
				String s2 = reader.readLine();
				stringList.addAll(List.of(s2.split(" ")));
			}
			String[] split = stringList.toArray(new String[stringList.size()]);

			PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
			PriorityQueue<Integer> minHeap = new PriorityQueue<>((a1, a2) -> a2 - a1);
			System.out.println(num / 2 + 1);
			for (int i = 0; i < num; i++) {
				String str = split[i];
				int val = Integer.parseInt(str);
				int minHeapSize = minHeap.size();
				int maxHeapSize = maxHeap.size();
				if (i % 2 == 0) { // 홀수번째인 경우
					if (minHeapSize == 0) {
						minHeap.add(val);
						System.out.print(val + " ");
						size += 1;
					} else {
						int left = minHeap.poll();
						int right = maxHeap.poll();
						List<Integer> tmpList = Arrays.asList(left, right, val);
						tmpList.sort((a1, a2) -> a1 - a2);
						left = tmpList.get(0);
						int mid = tmpList.get(1);
						right = tmpList.get(2);

						if (size % 10 == 0) {
							System.out.println();
						}
						size += 1;
						System.out.print(mid + " ");
						minHeap.add(left);
						minHeap.add(mid);
						maxHeap.add(right);

						print(minHeap, "minHeap");
						print(maxHeap, "maxHeap");
					}

				} else {
					Integer poll = minHeap.poll();
					int left = min(poll, val);
					int right = max(poll, val);
					minHeap.add(left);
					maxHeap.add(right);
					print(minHeap, "minHeap");
					print(maxHeap, "maxHeap");
				}

			}
			System.out.println();
		}
	}

	public static void print(PriorityQueue<Integer> v, String s) {
		// System.out.println(s);
		// for (var a : v) {
		// 	System.out.println(a);
		// }
	}
}
