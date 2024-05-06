import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCountTest {
    public WordCountTest() {
    }
public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    String[] otherArgs = (new GenericOptionsParser(conf,
    args)).getRemainingArgs();
    if(otherArgs.length < 2) {
    System.err.println("Usage: wordcount <in> [<in>...]
    <out>");
    System.exit(2);
    }
    Job job = Job.getInstance(conf, "word count test");
    job.setJarByClass(WordCountTest.class);
    job.setMapperClass(WordCountTest.TokenizerMapper.class)
    ;
    job.setCombinerClass(WordCountTest.IntSumReducer.class)
    ;
    job.setReducerClass(WordCountTest.IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    for(int i = 0; i < otherArgs.length - 1; ++i) {
        FileInputFormat.addInputPath(job, new Path("/home/hfut/jingdongcom_p.txt"));
        }
    FileOutputFormat.setOutputPath(job, new
    Path("/home/hfut/output_jingdong.txt"));
    System.exit(job.waitForCompletion(true)?0:1);
    }

    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();
        public IntSumReducer() {
        }
        public void reduce(Text key, Iterable<IntWritable> values, Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
            int sum = 0;
            IntWritable val;
            for(Iterator itr = values.iterator(); itr.hasNext();
            sum += val.get()) {
                val = (IntWritable)itr.next();
            }
            this.result.set(sum);
            context.write(key, this.result);
        }
    }
    public static class TokenizerMapper extends Mapper<Object,
    Text, Text, IntWritable> {
        private static final IntWritable one = new IntWritable(1);
        private Text word = new Text();
        public TokenizerMapper() {
        }
        public void map(Object key, Text value, Mapper<Object,
        Text, Text, IntWritable>.Context context) throws IOException,InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while(itr.hasMoreTokens()) {
            this.word.set(itr.nextToken());
            context.write(this.word, one);
    }
    }
    }
}