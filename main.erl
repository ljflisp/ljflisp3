-module(main).
-export([list/1, start/0]).

list(To_be_sorted) -> sort(To_be_sorted, [], true).

start() ->
  List = "a38xbkssj482",
  Sorted = list(List),
  io:fwrite("List ~p is sorted ~p~n", [List, Sorted]).

sort([], Acc, true) -> lists:reverse(Acc);
sort([], Acc, false) -> sort(lists:reverse(Acc), [], true);
sort([X, Y | T], Acc, _Done) when X > Y -> sort([X | T], [Y | Acc], false);
sort([X | T], Acc, Done) -> sort(T, [X | Acc], Done).
