package com.AbbonamentiPalestra.Class;

import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Entity
@Table(name = "Recensioni")
public class Recensioni {

	 @Id
	 @GeneratedValue(strategy = GenerationType.IDENTITY)
	 private Long id;

	 @ManyToOne
	 @JoinColumn(name = "abbonato_id", nullable = false)
	 private Abbonati abbonato;

	 @Column(nullable = false)
	 private String commento;
	 @Column(nullable = false)
	 private int valutazione;
	 @Column(nullable = false)
	 private LocalDate data; 
	
}
