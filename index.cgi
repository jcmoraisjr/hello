#!/bin/bash
while read -r e; do export "$e"; done < /tmp/env.var
buildcustom() {
  local datatype=$1
  local vardataname=$2
  local vardata=${!vardataname}
  if [ -n "$vardata" ]; then
    # title of the row (first column)
    local rowtitle=${vardata%%:*}
    # what the user wants (a varname or a command)
    local dataref=${vardata#*:}
    case "$datatype" in
      var)
        local varvalue=${!dataref}
        rowdata+=("${rowtitle}:${varvalue:-undef}")
        ;;
      cmd)
        local cmdout=$(eval $dataref 2>&1)
        rowdata+=("${rowtitle}:${cmdout}")
        ;;
      *)
        return 1
        ;;
    esac
    return 0
  else
    return 1
  fi
}
trow() { echo "<tr><td align=\"right\"><strong>$1</strong></td><td><pre style=\"margin: 0px;\">$2</pre></td></tr>"; }
encode() { sed 's^<^\&lt;^g;s^>^\&gt;^g'; }
psaux=$(ps aux)
ipaddr=$(ip a)
rowdata=()
i=1
while buildcustom "var" "VAR$i"; do
  ((i++))
done
i=1
while buildcustom "cmd" "CMD$i"; do
  ((i++))
done
echo "Content-Type: text/html"
echo
cat <<EOF
<!DOCTYPE html>
<html>
  <div align="center">
    <h2>Hello from $(hostname)</h2>
    <table border="1" cellpadding="6" cellspacing="0">
      <tbody>
        $(
          trow "hostname:" "$(hostname -f)"
          trow "date:" "$(date)"
          trow "timezone:" "${TZ:-Undefined}"
          trow "timezone offset:" "$(date -R | sed -r 's/.*([+-][0-9]{4})$/\1/')"
          trow "Remote:" "$REMOTE_ADDR"
          [ -n "$HTTP_X_FORWARDED_FOR" ] && trow "X-Forwarded-For:" "$HTTP_X_FORWARDED_FOR"
          trow "process:" "$(echo "$psaux" | encode)"
          trow "ip addr:" "$(echo "$ipaddr" | encode)"
          for r in "${rowdata[@]}"; do
            trow "${r%%:*}:" "${r#*:}"
          done
        )
      </tbody>
    </table>
  </div>
</html>
EOF
