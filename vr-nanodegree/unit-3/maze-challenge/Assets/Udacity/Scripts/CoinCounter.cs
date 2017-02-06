using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CoinCounter : MonoBehaviour {

	public Text countText;
	public Text allCoinsText;
	private static int coinsCollected;

	void Start ()
	{
		coinsCollected = 0;
		countText.text = "You have 0/5 coins";
		allCoinsText.text = "";
	}

	void Update ()
	{
		SetCoinText ();
	}

	// Coin counter is executed by an event trigger on the coin object
	private void CoinIncrementer()
	{	
		Debug.Log ("Triggered the coincount method");
		coinsCollected += 1;
		SetCoinText();
	}

	void SetCoinText ()
	{	
		if (coinsCollected >= 5) {
			countText.text = "";
			allCoinsText.text = "You've collected all the coins";
			Debug.Log ("User has collected all coins");
		} 
		else
		{
			countText.text = "You have " + coinsCollected + "/5 coins";
		}
	}
}