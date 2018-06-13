#!/usr/bin/perl
##!"C:\xampp\perl\bin\perl.exe" #windows(xampp用)

#cokiee名
$COOKIENAME = "count";
#保存時間（秒）
$COOKIELIFE = 5;
#訪問回数上限
$MAX_COUNT = 3;

$count = 0;

# cokiee取得
foreach $pair (split(/;\s*/, $ENV{'HTTP_COOKIE'})) {
    my ($name, $cookie) = split(/=/, $pair);
    if($name eq $COOKIENAME) {
        $count = $cookie;
        last;
    }
}

# cokiee作成
$count++;
@mon = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
@wdy = qw(Sun Mon Tue Wed Thu Fri Sat);
$life = $COOKIELIFE;
($sec, $min, $hour, $day, $mon, $year, $wday) = gmtime(time + $life);
$expires = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT", $wdy[$wday], $day, $mon[$mon], $year + 1900, $hour, $min, $sec);

# HTML出力
print "Content-type: text/html\n";
print "Set-Cookie: $COOKIENAME=$count; expires=$expires;\n\n";    #cokiee書き込み
print "<html>\n";
print "<head>\n";
print "<title>訪問回数</title>\n";
print "</head>\n";
print "<body>\n";
print " $count 回目のアクセス<br>\n";
if($count ge $MAX_COUNT) {
	print " $MAX_COUNT 回以上はアクセスできません。$COOKIELIFE 秒待ってからアクセスし直してください。<br>";
} else {
	print "ようこそ！！";
}
print "</body>\n";
print "</html>\n";

exit;
