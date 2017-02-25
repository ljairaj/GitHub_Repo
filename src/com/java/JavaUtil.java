package com.java;

public class JavaUtil {
	/*
	 * The method checks if the input string contains a # symbol. If # symbol exists then need to decrypt else encrpt.
	 */
	public static void main(String args[]) {
		String strNm = "Vimal";
		String strOut = null;
		String[] arrStrVal = null;
		
		System.out.println("Input: "+strNm);
		
		try {
			if(strNm.indexOf('#')!=-1) {
				arrStrVal = getSplitNms(strNm,"#");
			} else {
				arrStrVal = getSplitNms(strNm,null);
			}
			
			strOut = flipWords(arrStrVal);
			
			System.out.println("Output: "+strOut);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	/*
	 * The below method only splits the file into 2 portion.
	 * Can also include the condition to add # to the name of second part.
	 */
	private static String[] getSplitNms(String strInput, String sDelimit) throws Exception {
		
		String[] arrStrOut = new String[2];
		int iHlfPt = 0;
		
		if((strInput==null) || strInput.equals(""))
			return null;
		
		if(sDelimit!=null) {
			iHlfPt = strInput.indexOf(sDelimit);
			arrStrOut[0] = strInput.substring(0, iHlfPt);
			arrStrOut[1] = strInput.substring(iHlfPt+1, strInput.length());
		} else if((strInput.length()%2) == 0) {
			iHlfPt = strInput.length() / 2;
			arrStrOut[0] = strInput.substring(0, iHlfPt);
			arrStrOut[1] = strInput.substring(iHlfPt, strInput.length());
		} else {
			iHlfPt = (strInput.length() / 2) + 1;
			arrStrOut[0] = strInput.substring(0, iHlfPt);
			arrStrOut[1] = strInput.substring(iHlfPt, strInput.length())+"#";
		}
		
		return arrStrOut;
	}
	
	/*
	 * Encrypt Method
	 * Joins the 2 split words. 
	 */
	private static String flipWords(String[] arrString) {
		if(arrString.length == 2) {
			return arrString[1]+arrString[0];
		} else {
			return null;
		}
	}

}
