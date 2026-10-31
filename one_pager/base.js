document.querySelectorAll('[data-copy]').forEach(function(b){
  b.addEventListener('click',function(){
    var id=b.getAttribute('data-copy'),el=document.getElementById(id),ok=document.getElementById(id+'-ok'),t=el.textContent.trim();
    function sel(){var r=document.createRange();r.selectNodeContents(el);var s=window.getSelection();s.removeAllRanges();s.addRange(r);}
    function done(m){ok.textContent=m;ok.hidden=false;setTimeout(function(){ok.hidden=true},2500);}
    try{navigator.clipboard.writeText(t).then(function(){done('Copied')},function(){sel();done('Selected. Press Ctrl+C or Cmd+C')});}catch(e){sel();done('Selected. Press Ctrl+C or Cmd+C')}
  });
});
window.addEventListener('beforeprint',function(){document.querySelectorAll('details').forEach(function(d){d.open=true;});});
function openFromHash(){try{var id=decodeURIComponent(location.hash.slice(1));var t=id&&document.getElementById(id);var d=t&&t.closest('details');if(d)d.open=true;}catch(e){}}
window.addEventListener('hashchange',openFromHash);openFromHash();
