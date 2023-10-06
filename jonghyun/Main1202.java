import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class Main1202 {


	public static void main(String[] args) throws IOException {

		PriorityQueue<long[]> priorityQueue = new PriorityQueue<>((a1, a2) -> (int)(a2[0] - a1[0]));
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		var input = reader.readLine();
		var split = Arrays.stream(input.split(" ")).mapToLong(Long::new).toArray();
		Long N = split[0];
		Long K = split[1];

		TreeMap<Long, Long> bags = new TreeMap<>();
		for (Long i =0L; i< N; i++) {
			var input1 = reader.readLine();
			var li = Arrays.stream(input1.split(" ")).mapToLong(Long::new).toArray();
			var v1 = li[0];
			var v2 = li[1];
			li[0] = v2;
			li[1] = v1;
			priorityQueue.add(li);
		}

		for (Long i =0L; i< K; i++) {
			var input2 = Long.parseLong(reader.readLine());
			bags.merge(input2, 1L, Long::sum);
		}
		Long answer = 0L;
		while (!priorityQueue.isEmpty()) {
			var v = priorityQueue.poll();
			var vi = v[0];
			var mi = v[1];
			Map.Entry<Long, Long> entry = bags.ceilingEntry(mi);
			if (entry != null) {
				Long floor = entry.getKey();
				if (entry.getValue() == 1) {
					bags.remove(floor);
				} else {
					bags.put(floor, bags.get(floor) - 1);
				}

				answer += vi;
			}
		}
		System.out.println(answer);

	}
}
