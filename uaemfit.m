function uaemfit(x,y,n)
  lenx=length(x);
  leny=length(y);
  one=ones(lenx,n);
  switch n
    case n=1
      A1=[one(:,1),x'];
      u1=inv((A1'*A1))*A1'*y';
      y1=u1(2,1)*x+u1(1,1);
      scatter(x,y1)
      grid
      hold on
    case n=2
      A2=[one(:,1),x',power(x,2)'];
      u2=inv((A2'*A2))*A2'*y'
      y2=u2(3,1)*power(x,2)+u2(2,1)*x+u2(1,1);
      d=[x',y',y2'];
      scatter(x,y2)
      hold on
      plot(x,y)
    case n=3
      A3=[one(:,1),x',power(x,2)',power(x,3)'];
      u3=inv((A3'*A3))*A3'*y'
      y3=u3(4,1)*power(x,3)+u3(3,1)*power(x,2)+u3(2,1)*x+u3(1,1);
      scatter(x,y3)
  endswitch
endfunction
  
