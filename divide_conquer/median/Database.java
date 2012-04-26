
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Random;
import java.util.Set;
import java.util.TreeSet;

public class Database {

    public static final int DEFAULT_SIZE = 100;
    private static Database database1 = null;
    private static Database database2 = null;
    private static boolean initialized = false;

    public static void Initialize( int numElements ) {
        HashSet<Integer> allNumbers = new HashSet<Integer>();
        Set<Integer> db1 = new HashSet<Integer>();
        Set<Integer> db2 = new HashSet<Integer>();
        Random random = new Random();
        int totalSize = 2 * numElements;
        while( allNumbers.size() < totalSize ) {
            allNumbers.add( random.nextInt( 100000 ) );
        }
        Iterator<Integer> iter = allNumbers.iterator();
        while( totalSize > numElements ) {
            db1.add( iter.next() );
            totalSize--;
        }
        while( iter.hasNext() ) {
            db2.add( iter.next() );
        }

        database1 = new Database( db1 );
        database2 = new Database( db2 );

        Set sorted = new TreeSet<Integer>( allNumbers );
        System.out.println( "The true median is " + sorted.toArray()[numElements-1] );

        initialized = true;
    }

    public static Database getDatabase1() {
        if(!initialized) Initialize(DEFAULT_SIZE);
        return database1;
    }

    public static Database getDatabase2() {
        if(!initialized) Initialize(DEFAULT_SIZE);
        return database2;
    }

    private Integer[] database = null;

    Database( Set<Integer> values ) {
        database = values.toArray(new Integer[0]);
        Arrays.sort(database);
    }

    Integer getKthLargestValue(int k) {
        return database[k-1];
    }
}
