public static class MyPartitioner extends Partitioner<Text,Text>{
    public int getPartition(Text key, Text value, int numReduceTasks){

        if(numReduceTasks==0){
            return 0;
        }
        if(key.equals(new Text("2013"))){
            return 0;
        }
        if(key.equals(new Text("2014"))){
            return 1;
        }
        if(key.equals(new Text("2015"))){
            return 2;
        }
        if(key.equals(new Text("2016"))){
            return 3;
        }
        if(key.equals(new Text("2017"))){
            return 4;
        }
        if(key.equals(new Text("2018"))){
            return 5;
        }
        if(key.equals(new Text("2019"))){
            return 6;
        }
        if(key.equals(new Text("2020"))){
            return 7;
        }
        if(key.equals(new Text("2021"))){
            return 8;
        }
    }
}