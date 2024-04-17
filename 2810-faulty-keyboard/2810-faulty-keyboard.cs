public class Solution {
    public string FinalString(string s) {
        var sb = new StringBuilder();
        for(int i = 0; i < s.Length; i++)
        {
            if(s[i] != 'i')
            {
                sb.Append(s[i]);
            }else{
                var sb1 = new StringBuilder(sb.Length);
                sb1.Append(sb);
                //sb.Clear();
                sb.Length = 0;
                for (int j = sb1.Length - 1; j >= 0; j--)
                {
                    sb.Append(sb1[j]);
                }
            }
        }
        return sb.ToString();
    }
}